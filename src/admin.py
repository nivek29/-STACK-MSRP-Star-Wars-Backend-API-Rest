import os
from flask_admin import Admin
from models import db, Character, Properties_Character, Profile, Properties_Profile, Planet, Properties_Planet
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Properties_Character, db.session))
    admin.add_view(ModelView(Profile, db.session))
    admin.add_view(ModelView(Properties_Profile, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Properties_Planet, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))