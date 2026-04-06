from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import instaloader
import re
import os

TOKEN = "8413626359:AAEgylKKWKhJIgGgUDuRdCq-87RBeK2AKK8"

L = instaloader.Instaloader()

async def download_instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" not in text:
        await update.message.reply_text("❌ Instagram link yubor!")
        return

    try:
        shortcode = re.search(r"\/(reel|p|tv)\/([^\/]+)", text).group(2)
        
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target="downloads")

        for file in os.listdir("downloads"):
            if file.endswith(".mp4"):
                video_path = os.path.join("downloads", file)
                
                await update.message.reply_video(video=open(video_path, 'rb'))
                
                os.remove(video_path)

    except Exception as e:
        await update.message.reply_text("❌ Xatolik: " + str(e))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_instagram))

print("Bot ishga tushdi...")
app.run_polling()
