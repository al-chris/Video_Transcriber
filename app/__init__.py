import os
from flask import Flask

app = Flask(__name__)

# app.secret_key= os.environ.get('SECRET_KEY')
app.secret_key = 'secrt'

# limit to files below 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
UPLOAD_FOLDER_AUDIO = os.path.join(path, r'app\static\audio')

# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER_AUDIO'] = UPLOAD_FOLDER_AUDIO

UPLOAD_FOLDER_VIDEO = os.path.join(path, r'app\static\videos')
app.config['UPLOAD_FOLDER_VIDEO'] = UPLOAD_FOLDER_VIDEO

UPLOAD_FOLDER_TEXT = os.path.join(path, r'app\static\transcriptions')
app.config['UPLOAD_FOLDER_TEXT'] = UPLOAD_FOLDER_TEXT


from app import views
from app import models