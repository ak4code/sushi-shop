from decouple import config
import vk
import uuid

session = vk.Session(access_token=config('VK_KEY'))
api = vk.API(session, v='5.92', lang='ru', )
ADMIN_ID = config('ADMIN_ID')


def get_random_id():
    return uuid.uuid4().int
