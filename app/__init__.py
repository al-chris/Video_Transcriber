import os
from flask import Flask

app = Flask(__name__)

# app.secret_key= os.environ.get('SECRET_KEY')
app.secret_key = 'secrt'

# limit to files below 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



from app import views
from app import models