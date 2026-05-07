import telebot, requests, re, threading, time

# 🔱 SULTAN V-GOD: KOYEB REBORN 2026 🔱
# NAYA TOKEN INJECTED
TOKEN = '8576160850:AAF14hRkZYK-icIhdfLEJe1TTY5kQRUUCUQ'
bot = telebot.TeleBot(TOKEN)

# 🛡️ PURANE SESSIONS KA KHATMA (ANTI-CONFLICT)
try:
    bot.delete_webhook()
    print("🔱 Old sessions purged. Ready for strike.")
except: pass

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔱 **SULTAN REBORN: KOYEB ACTIVE** 🔱\n━━━━━━━━━━━━━━\nBhai, naye token ke saath tabaahi shuru!")

@bot.message_handler(func=lambda m: True)
def strike(m):
    status = bot.reply_to(m, "⚡ **Scraping VIP Global Nodes...**")
    hits = []
    
    def fetch(u):
        try:
            r = requests.get(u, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            found = re.findall(r'\+91\d{10}', r.text)
            hits.extend(found)
        except: pass

    # High-Velocity Threads
    nodes = [
        "https://api.internal-node.in/v10/access", 
        "https://gsm-gateway.secure-auth.in/v4/fresh-msisdn",
        "https://private.receive-sms.cc/vip-india/"
    ]
    
    threads = [threading.Thread(target=fetch, args=(u,)) for u in nodes]
    for t in threads: t.start()
    for t in threads: t.join(timeout=5)
    
    if hits:
        res = "🔱 **CORE LEAKS ACQUIRED** 🔱\n\n" + "\n".join(list(set(hits))[:35])
        bot.edit_message_text(res, m.chat.id, status.message_id)
    else:
        bot.edit_message_text("❌ Node Shielded. Try again in 5s!", m.chat.id, status.message_id)

# ♾️ IMMORTAL POLLING
if __name__ == "__main__":
    print("🔱 Sultan is rising on Koyeb with New Token...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
