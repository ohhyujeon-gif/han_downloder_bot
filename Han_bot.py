import os
from telegram.ext import Updater, CommandHandler
import subprocess

def download(update, context):
    if not context.args:
        update.message.reply_text("Usage: /download <video_url>")
        return

    url = context.args[0]
    update.message.reply_text(f"Downloading video from {url} ...")

    try:
        output_file = "video.mp4"
        subprocess.run(["yt-dlp", "-o", output_file, url], check=True)

        with open(output_file, "rb") as video:
            update.message.reply_video(video)

        os.remove(output_file)
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

def main():
    bot_token = os.getenv("BOT_TOKEN")  # BOT_TOKEN Render ke env vars me set karna hoga
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("download", download))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
