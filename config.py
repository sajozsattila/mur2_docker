import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    NAME = "mur2_docker"
    VERSION = '1.0.0'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SESSION_COOKIE_NAME = 'mur2.co.uk'
    # DB settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSL_DIR = "/home/mur2/npm/src/csl/"
    # supported languages
    LANGUAGES = ['en', 'hu', 'es', 'zh_CN', 'ru', 'zh_TW', 'zh_HK', 'zh_Hant_TW', 'zh_Hant_HK']
    # wordpress.com app settings
    APP_WORDPRESSCOM_ID = '68742'
    APP_WORDPRESSCOM_PASSWORD = 'Qr3ZSE0n8XzhrJJ2KlTplnThh97oVJqCB6L1yixaxOFfo3QXCJQTrVOgdOLGmw5k'
    # upload for users
    UPLOAD_FOLDER = "/home/mur2/user_data"
    UPLOADED_PHOTOS_DEST = "/home/mur2/user_data"
