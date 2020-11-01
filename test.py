import youtube_dl
import telebot


bot = telebot.TeleBot('1128890684:AAHcQE-p8CdKl-sGENipRxxsRrDRU9MF290')
links = {}

def youtube(url):
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        res = ydl.extract_info(url, download=False)
        return res['url']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, send me a video link")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    link = youtube(message.text)
    bot.reply_to(message, link)


print('Start bot')
bot.polling()
# ydl_opts = {
# 'format': 'bestaudio/best',
# 'postprocessors': [{
#     'key': 'FFmpegExtractAudio',
#     'preferredcodec': 'mp3',
#     'preferredquality': '192',}],}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     res = ydl.extract_info(url, download=False)
# return res['url']
