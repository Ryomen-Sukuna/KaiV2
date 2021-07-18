if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    sys.exit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    # If you dont know, run the bot and do /id in your private chat with it
    OWNER_ID = "YOUR ID HERE"
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    # needed for any database modules
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    # List of id's (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = []
    # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = []
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_USERS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
