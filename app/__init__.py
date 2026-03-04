

from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate

from app.public.routes.home_routes import home_bp
from app.public.routes.sivm_routes import sivm_bp
from app.public.routes.aci_routes import aci_bp
from app.public.routes.blog_routes import blog_bp
from app.public.routes.contact_routes import contact_bp
from app.public.routes.partner_routes import partner_bp

from app.admin.routes.admin_routes import admin_bp
from app.admin.routes.auth import auth_bp
from app.admin.routes.blog_admin import blog_admin_bp
from app.admin.routes.actualite_admin import actualite_admin_bp

from app.user.routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    
    app.register_blueprint(home_bp)
    app.register_blueprint(sivm_bp)
    app.register_blueprint(aci_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(partner_bp)

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_admin_bp)
    app.register_blueprint(actualite_admin_bp)
    
    app.register_blueprint(user_bp)
    

    
    
    return app