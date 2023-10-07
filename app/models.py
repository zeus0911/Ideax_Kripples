from email.policy import default
from pyexpat import model
from unicodedata import decimal
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator
import PIL 
from PIL import Image

STATUS_CHOICE = (
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)

STATUS = (
    ("draft","Draft"),
    ("disable", "Disable"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("publish","Published"),
)

RATING = (
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.vid, filename)

def category_directory_path(instance, filename):
    return 'category_{0}/{1}'.format(instance.cid, filename)

def product_directory_path(instance, filename):
    return 'product_{0}/{1}'.format(instance.pid, filename)

def file_directory_path(instance, filename):
    return 'file_{0}/{1}'.format(instance.pid, filename)

# Create your models here.
class Category(models.Model):
    cid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix ="cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=category_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'svg'])]
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"


    def category_image(self):
        return mark_safe('<img src = "%s" width = "50" height ="50">'% (self.image.url))
    
    def __str__(self):
        return self.title
    
class CategoryImages(models.Model):
    images = models.ImageField(upload_to="category_images", default="product.jpg")
    product = models.ForeignKey(Category, related_name="c_image", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Catgory Images"

    
class Tags(models.Model):
    pass
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True,length = 10, max_length = 20, prefix ="ven", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"


    def vendor_image(self):
        return mark_safe('<img src = "%s" width = "50" height ="50">'% (self.image.url))
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True,length = 10, max_length = 20, prefix ="pro", alphabet = "abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_directory_path)
    description = models.TextField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Saving the model instance first

    #     # Open the image using self
    #     img = Image.open(self.image.path)

    #     # Resize the image to a fixed size of 300x300 pixels
    #     new_img = img.resize((300, 500),  PIL.Image.Resampling.LANCZOS)
        
    #     # Save the resized image back to the same path
    #     new_img.save(self.image.path)

    specifications = models.TextField(null=True, blank=True)
    #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    tags = TaggableManager(blank = True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    featured = models.BooleanField(default=True)

    sku = ShortUUIDField(unique = True, length = 4, max_length = 10, prefix = "sku", alphabet = "1234567890")

    date = models.DateTimeField(null=True,blank=True)

    file = models.FileField(
        upload_to= file_directory_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'pdf', 'png'])
        ],
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Products"


    def product_image(self):
        return mark_safe('<img src = "%s" width = "50" height ="50">'% (self.image.url))
    
    def __str__(self):
        return self.title

    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="p_image", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="review")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Review"
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlist"
    
    def __str__(self):
        return self.product.title
    




    





    


    

    
