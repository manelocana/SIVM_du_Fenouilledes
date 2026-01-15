

from flask import Flask

from app.routes.home_routes import home_bp
from app.routes.estefan_routes import estefan_bp
from app.routes.julien_routes import julien_bp
from app.routes.blog_routes import blog_bp
from app.routes.contact_routes import contact_bp




def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(estefan_bp)
    app.register_blueprint(julien_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)

    
    
    
    return app