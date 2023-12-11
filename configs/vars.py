import os
from configparser import ConfigParser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(ROOT_DIR)

cfg = ConfigParser()
cfg.read(os.path.join(ROOT_DIR, "env.ini"))

PORT = cfg.get("default", "port")
TLS = cfg.get("default", "tls")
# Outlook
OUTLOOK_SERVER = cfg.get("outlook", "server")
OUTLOOK_EMAIL = cfg.get("outlook", "username")
OUTLOOK_PASSWORD = cfg.get("outlook", "password")

# Gmail
GMAIL_SERVER = cfg.get("gmail", "server")
GMAIL_EMAIL = cfg.get("gmail", "username")
GMAIL_PASSWORD = cfg.get("gmail", "password")
