import telegram
from config.auth import telegram_bot_token, telegram_group_chatid


def sendMsg(ID=telegram_group_chatid, msg=''):
    """
    Send Telegram Text Message to selected ID.
    """

    bot = telegram.Bot(token=telegram_bot_token)

    bot.sendMessage(chat_id=ID,
                    text=f'{msg}')


def sendImg(ID=telegram_group_chatid, caption='', img=''):
    """
    Send Telegram IMG Message to selected ID.
    """

    bot = telegram.Bot(token=telegram_bot_token)


    bot.sendPhoto(chat_id=ID,
                  caption=caption,
                  photo=open(img, 'rb'))

sendMsg(ID=telegram_group_chatid, msg='Comment alez vous?')
