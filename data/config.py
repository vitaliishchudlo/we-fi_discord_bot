import os

from dotenv import load_dotenv

PATH_ENV_FILE = '.env'

load_dotenv(PATH_ENV_FILE)

# # # # # # # # # # # # # # # # # # # # # # #
#                 Variables:                #
# # # # # # # # # # # # # # # # # # # # # # #

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

BOT_PREFIX = '.'
CAPTCHA_PREFIX = 'WeFi$'

ID_OWNER = 398567252061978628
ID_ROLE_ADMIN = 830456241116938310
ID_ROLE_MODERATOR = 952960220714401863

ID_CHAT_ACHIEVEMENT_STATISTICS = 916003184063963176
ID_CHAT_ACHIEVEMENT_INFO = 917522912980893757
ID_ROLE_ACHIEVEMENTS = 952280483759292456  # WeFi
ID_ROLE_OTHER = 952282700780281938  # Other

ID_CHAT_WELCOME = 952278528458641438

DEFENDED_CHATS = [
    ID_CHAT_ACHIEVEMENT_STATISTICS,
    ID_CHAT_ACHIEVEMENT_INFO
]

ID_ROLES_ACHIEVEMENTS_EDITORS = [
    ID_ROLE_ADMIN,
    ID_ROLE_MODERATOR
]

TEST_LIST = [
    ID_ROLE_ADMIN,
    ID_ROLE_MODERATOR,
    ID_ROLE_ACHIEVEMENTS
]

PATH_DATABASE = 'database/database.db'

CAPTCHA_BODY = [
    'Putin Xyilo',
    'Love Ukraine',
    'No Russia'
]


VERSION_PREFIX = 'TESTING'
VERSION_NUBMER = ''
