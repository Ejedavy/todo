from datetime import datetime, timedelta
import random
from django.core.cache import cache


class Token:

    def __init__(self, value):
        self.value = value
        self.deadline = datetime.now() + timedelta(minutes=15)

    @property
    def is_expired(self):
        return datetime.now() > self.deadline

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class TokenGenerator:

    def make_token(self, user, **kwargs):
        value = str(random.randint(100000, 999999))
        token = Token(str(value))
        cache.set(value, [str(user.id), token.deadline])
        return token

    def check_token(self, user, token):
        original_user = cache.get(token)[0]
        deadline = cache.get(token)[1]
        if datetime.now() > deadline:
            return False
        if str(user.id) == original_user:
            return True
        else:
            return False


token_generator = TokenGenerator()
