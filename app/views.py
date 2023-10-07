from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count, Avg
from app.models import Product, Category, Vendor, ProductImages, ProductReview, Wishlist
from .forms import ProductForm
from ocr import *
import os

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data
            product = form.save()

            # Check if a file is uploaded
            if product.file:
                # Determine the file extension
                file_extension = os.path.splitext(product.file.name)[-1].lower()

                # Determine the language based on the category
                category = product.category.title if product.category else None
                if category == "Nepali":
                    language = 'ne'
                elif category == "Maithili":
                    language = 'mai'
                elif category == "Newari":
                    language = 'new'
                else:
                    # Default to English if category is not specified or unknown
                    language = 'eng'

                if file_extension in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'):
                    # It's an image, so read text from the image
                    image = Image.open(product.file)
                    text = read_text_from_pillow_image(image, language)
                elif file_extension == '.pdf':
                    # It's a PDF, so extract text from the PDF
                    text = extract_text_from_scanned_pdf(product.file.path, language)
                else:
                    # Handle other file types or show an error message
                    text = "Unsupported file type"

                # Update the product's description with the extracted text
                product.description = text
                product.save()
            
            return render(request, 'add_product.html', {'form': form, 'text': text})
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'add_product.html', context)


def index(request):
    products = Product.objects.filter(featured = True).order_by('-date')
    categories = Category.objects.filter()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, 'Index.html', context)

def product_view_list(request):
    products = Product.objects.filter(featured = True).order_by('-date')

    context = {
        "products": products
    }

    return render(request, 'product_list.html', context)

def category_view_list(request):
    categories = Category.objects.filter()
    categories = Category.objects.annotate(product_count=Count('product'))

    context = {
        "categories": categories
    }

    return render(request, 'category_list.html', context)

def category_detail(request, category_cid):
    category = get_object_or_404(Category, cid=category_cid)
    category_images = category.c_image.all()
    context = {
        'category': category, 
        'category_images': category_images
    }
    return render(request, 'category_list.html', context)

def category_detail_view(request, cid):
    category = get_object_or_404(Category, cid=cid)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category-detail.html', context)




def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    #product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid = pid)
    categories = Category.objects.filter()

    p_image = product.p_image.all()

    review = ProductReview.objects.filter(product = product).order_by('-date')

    average_review = ProductReview.objects.filter(product = product).aggregate(rating = Avg('rating'))

    context = {
        "product" : product,
        "p_image" : p_image,
        "average_review" : average_review,
        "categories" : categories,
        "review" : review,
        "products" : products,
    }

    return render(request, 'product-detail.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')





