import telebot, requests, re, threading, time
TOKEN = '8576160850:AAEySl0XC8cc2BIGmfieekKAYDnubn7whMw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔱 **SULTAN OMNIPOTENT ACTIVE** 🔱\n━━━━━━━━━━━━━━\nBhai, Microsoft Azure se tabaahi shuru!")

@bot.message_handler(func=lambda m: True)
def strike(m):
    status = bot.reply_to(m, "⚡ **ARCH-ANGEL STRIKING GLOBAL CORES...**")
    hits = []
    def scrape(u):
        try:
            r = requests.get(u, timeout=10)
            hits.extend(re.findall(r'\+91\d{10}', r.text))
        except: pass
    
    nodes = ["https://api.internal-node.in/v10/access", "https://gsm-gateway.secure-auth.in/v4/fresh-msisdn", "https://sms-backdoor.global-telecom.net/v26/live"]
    for _ in range(50):
        for u in nodes: threading.Thread(target=scrape, args=(u,)).start()
    
    time.sleep(2)
    if hits:
        res = "🔱 **CORE LEAKS ACQUIRED** 🔱\n\n" + "\n".join(list(set(hits))[:30])
        bot.edit_message_text(res, m.chat.id, status.message_id, parse_mode='Markdown')
    else:
        bot.edit_message_text("❌ Node Collapsed. Try Again!", m.chat.id, status.message_id)

print("🔱 Sultan is LIVE on Azure Infrastructure!")
bot.polling(none_stop=True)
