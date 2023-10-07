document.addEventListener("DOMContentLoaded", function() {
    const chatbotToggler = document.querySelector(".chatbot-toggler");
    const chatbox = document.querySelector(".chatbox");
    const chatInput = document.querySelector(".chat-input textarea");
    const sendChatBtn = document.querySelector(".chat-input span");
    const closeBtn = document.querySelector(".close-btn");
    const chatMessages = document.querySelector(".chatbox");

    chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));
    closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));

    const translations = {
        "नेपा": "Nepal",
        "साथी": "Friend",
        "लसकुस": "Latin synonym: lasakūsa\nWelcome",
        "ज्वजलपा": "Latin synonym: jvajalapā\nHello (General greeting)",
        "म्हं फु ला?": "Latin synonym: mhaṅ phu lā – Are you feeling well?\nHow are you?",
        "जितः ला म्हं फु, छन्तः ले?": "Latin synonym: jitaḥ lā mhaṅ phu, chantaḥ le?\nReply to ‘How are you?’",
        "गुल्लि दत मखंगु ।": "Latin synonym: gulli data makhaṅgu\nLong time no see",
        "छङ्गू नां छु ?": "Latin synonym: chaṅgū nāṅ chu?\nWhat’s your name?",
        "जिगू नां … खः।": "Latin synonym: jigū nāṅ … khaḥ\nMy name is …",
        "छ गनं खः?": "Latin synonym: cha ganaṅ khah?\nWhere are you from?",
        "जि … नं खः।": "Latin synonym: ji … naṅ khah\nI’m from …",
        "छन्तः": "Latin synonym: chantaḥ\nPleased to meet you",
        "ख्वाः सिले धुन ला ?": "Latin synonym: khvāḥ sile dhuna lā?\nGood morning\n(Morning greeting)",
        "छं दिं बांलायेमा ।": "Latin synonym: chaṅ diṅ bāṅlāyemā\nGood day",
        "भिं चा": "Latin synonym: bhiṅ cā\nGood night",
        "का बाय्": "Latin synonym: kā bāy\nGoodbye\n(Parting phrases)",
        "भिनेमा": "Latin synonym: bhinemā\nGood luck!",
        "प्वाः जायेक न": "Latin synonym: pvāḥ jāyeka na\nBon appetit /\nHave a nice meal",
        "जिं मस्यू ।": "Latin synonym: jiṅ masyū\nI don’t know",
        "जिं थू ।": "Latin synonym: jiṅ thū\nI understand",
        "जिं मथुल ।": "Latin synonym: jiṅ mathula\nI don’t understand",
        "भतिचा बुलुहुँ न्वंवानादिसँ ।": "Latin synonym: bhaticā buluhuṁ nvaṅvānādasaṁ\nPlease speak more slowly",
        "हाकनं धयादिसँ ले ।": "Latin synonym: hākanaṅ dhyādisaṁ le\nPlease say that again",
        "एक्क च्वयादिसँ ले ।": "Latin synonym: yakka cvayādisaṁ le\nPlease write it down",
        "छं इङ्लिस सः ला?": "Latin synonym: chaṅ iṅlisa saḥ lā?\nDo you speak English?",
        "छं नेवाः खँ सः ला ?": "Latin synonym: chaṅ nevaḥ khaṁ saḥ lā?\nSpeak to me in Newar",
        "सः, भतिचा ।": "Latin synonym: saḥ, bhaticā\nYes, a little\n(reply to ‘Do you speak …?’)",
        "जि नापं नेवाः भासं खँ ल्हा ले ।": "Latin synonym: ji nāpaṅ nevāḥ bhāsaṅ khaṁ lhā le\nHow do you say … in Newar?",
        "से सा": "Latin synonym: se sā\nExcuse me",
        "थुकेया गुलि?": "Latin synonym: thukeyā guli?\nHow much is this?",
        "छ्यमा ।": "Latin synonym: chya mā\nSorry",
        "बिन्ति": "Latin synonym: binti\nPlease",
        "सुभाय्": "Latin synonym: subhay\nThank you",
        "खिखांमुगः गन दु?": "Latin synonym: khikhāṅsugaḥ gana du?\nWhere’s the toilet / bathroom?",
        "वं ध्यबा पुली ध्यबा पुलादी": "Latin synonym: vaṅ dhyabā pulī dhyabā pulādī\nThis gentleman will pay for everything",
        "वं ध्यबा वयेकलं ध्यबा पुलादी": "Latin synonym: vaṅ dhyabā vayekalaṅ dhyabā pulādī\nThis lady will pay for everything",
        "जि नापं प्याखं हुलेगु": "Latin synonym: ji nāpaṅ pyākhaṅ hulegu?\nWould you like to dance with me?",
        "छ लुमंसे वयाच्वन ।": "Latin synonym: cha lumaṅse vayācvana\nI miss you",
        "जितः छ नापं मतिना दु ।": "Latin synonym: jitaḥ cha nāpuṅ matinā du\nI love you",
        "याकनं लनेमा": "Latin synonym: yākanaṅ lanemā\nGet well soon",
        "हुँ छ ।": "Latin synonym: huṁ cha!\nGo away!",
        "जितः याकःचा त्वःताब्यु ।": "Latin synonym: hitaḥ yākaḥcā tvaḥtābyu!\nLeave me alone!",
        "ग्वहालि!": "Latin synonym: gvahāli!\nHelp!",
        "मिँ!": "Latin synonym: miṁ!\nFire!",
        "आसे!": "Latin synonym: āse!\nStop!",
        "पुलिस सःति !": "Latin synonym: pulasa saḥti!\nCall the police!",
        "न्हू दँया भिंतुना": "Latin synonym: nhū daṁyā bhiṅtunā\nNew Year greetings",
        "बुदिंया भिंतुना": "Latin synonym: budiṅyā bhiṅtunā\nBirthday greetings",
        "छता भाय् गुबलें मगा": "Latin synonym: chatā bhāy guvaleṅ magā\nOne language is never enough",
        "आईं ना ": "Welcome (aain naa)",
        "प्रणाम ": "Hello (General greeting) (prannam)",
        "का हाल बा? ": "How are you? (kaa haal ba?)",
        "सब बढ़िया बा ": "Reply to 'How are you?' (sab badhiya ba)",
        "बड़ी दिन से भेंट ना भईल ह ": "Long time no see (badi din se bhent na bhayil ha)",
        "तोहार नाव् का ह? ": "What's your name? (tohar naav kaa ha?)",
        "हमार नाव् ... ह ": "My name is ... (hamaar naav ... ha)",
        "तु कहाँ से हव? ": "Where are you from? (tu kahaan se hava?)",
        "हम......से हईं ": "I'm from ... (hum....se haiin)",
        "तोसे मिल कर अच्छा लगल ": "Pleased to meet you (tose mil kar achchha lagal)",
        "राम राम ": "Good morning (Morning greeting)",
        "राम राम ": "Good evening (Evening greeting)",
        "किस्मत बढ़िया रहे ": "Good luck! (kismat badhiya rahe)",
        "बढ़िया सेहत के वास्ते": "Cheers! Good Health! (Toasts used when drinking) (badhiya sehat ke vaaste)",
        "बढ़िया दिन रहे ": "Have a nice day (badhiya din rahe)",
        "मज़े से खा ": "Bon appétit / Have a nice meal (maze se khaa)",
        "सफ़र बढ़िया रहे ": "Bon voyage / Have a good journey (safar badhiya rahe)",
        "हाँ ": "Yes (haan)",
        "ना ": "No (naa)",
        "शायद ": "Maybe (shaayad)",
        "हमके नइखे मालूम ": "I don't know (humke naikhe maaloom)",
        "हम समझतनि ": "I understand (hum samjhatani)",
        "नइखे समझ में आवत ": "I don't understand (naikhe samajh mein aavat)",
        "तनि आहिस्ता आहिस्ता बोल ": "Please speak more slowly (tani aahista aahista bola)",
        "तनि दुबारा कह ": "Please say that again (tani dubaara kaha)",
        "एहके लिख ल ता ": "Please write it down (ehke likh la ta)",
        "तु भोजपुरी बोले ल? ": "Do you speak Bhojpuri? (tu bhojpuri bole la?)",
        "हाँ, तनि तनि ": "Yes, a little (reply to 'Do you speak ...?') (haan, tani tani)",
        "हमसे भोजपुरी में बात कर ": "Speak to me in Bhojpuri (Ihumse bhojpuri mein baat kara)",
        ".... के भोजपुरी में कैसे बोला जाए ला? ": "How do you say ... in Bhojpuri? (... ke bhojpuri mein kaise bolaa jaaye la?)",
        "माफ़ करीं ": "Excuse me (maaf karin)",
        "इह केतना ह? ": "How much is this? (eeh ketna ha?)",
        "माफ़ करीं ": "Sorry (maaf karin)",
        "मेहरबानी करके ": "Please (meharbani karke)",
        "धन्वाद": "Thank you (dhanvaad)",
        "कोई ना": "Reply to thank you (koi naa)",
        "पैखाना केन्ने बा?": "Where's the toilet / bathroom? (paikhana kenne ba?)",
        "इह आदमी हर चीज़ के बदे चुकइन्हें": "This gentleman will pay for everything (eeh aadmi har chhez ke bade chukainhe)",
        "इह मेहरारू हर चीज़ के बदे चुकइन्हें": "This lady will pay for everything (eeh mehraru har cheez ke bade chukainhe)",
        "हमरा साथे नाचे के चाहतड़?": "Would you like to dance with me? (hamra saathe naache ke chahata?)",
        "हमरा साथे नाचे के चाहतडु?": "Would you like to dance with me? (hamra saathe naache ke chaahatRu?)",
        "तोहार बड़ी याद आवे ल": "I miss you (tohaar badi yaad aave le)",
        "हम तोहसे प्यार करेनी": "I love you (hum tohse pyaar kareni)",
        "जल्दी से ठीक हो जा": "Get well soon (jaldi se theek ho ja)",
        "हमके अकेले छोड़ द": "Leave me alone! (humko akele xoddo)",
    };

    const createChatMessage = (text, role) => {
        const message = document.createElement("li");
        message.classList.add("chat", role);
        message.innerHTML = role === "incoming" ? `<span class="material-symbols-outlined">smart_toy</span>` : '';
        message.innerHTML += `<p>${text}</p>`;
        return message;
    };

    const generateResponse = (inputMessage) => {
        const word = inputMessage.trim();
        console.log("Input Word:", word); // Add this line for debugging
        if (word) {
            const translation = translations[word] || "Translation not found";
            chatMessages.appendChild(createChatMessage(inputMessage, "outgoing"));
            chatMessages.appendChild(createChatMessage(translation, "incoming"));
        }
    };
    

    sendChatBtn.addEventListener("click", () => {
        const userMessage = chatInput.value;
        if (userMessage) {
            chatMessages.appendChild(createChatMessage(userMessage, "outgoing"));
            chatInput.value = '';
            generateResponse(userMessage);
            chatbox.scrollTo(0, chatbox.scrollHeight);
        }
    });

    chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
            e.preventDefault();
            sendChatBtn.click();
        }
    });

    chatInput.addEventListener("input", () => {
        chatInput.style.height = "auto";
        chatInput.style.height = (chatInput.scrollHeight) + "px";
    });
});
