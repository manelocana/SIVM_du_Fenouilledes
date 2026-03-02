

from app import create_app



app = create_app()



""" 
usamos esto una vez, para crear la db
una vez usado la primera vez, lo comentamos.
from app.extensions import db
with app.app_context():
    db.create_all()
 """



if __name__ == '__main__':
    app.run(debug=True)