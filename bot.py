import telegram
from django.conf import settings


class Bot:
    def __init__(self):
        self.token = settings.BOT_TOKEN
        self.bot = telegram.Bot(token=self.token)

    def send_test(self):
        self.bot.sendMessage(chat_id=settings.BOT_TEST_ID,
                             text="Hello David this is a test")

    def send_account_creation_code(self, code, user):
        self.bot.sendMessage(chat_id=user,
                             text=f"Thanks for signing up for the task app."
                                  f" To activate your account enter the code below when prompted from the website."
                                  f"\nPlease note that this code expires in 15 minutes. If you did not request "
                                  f"for this kindly ignore.\nThe code is {code}")
