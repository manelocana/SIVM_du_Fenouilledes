

""" corremos esto en flask shell para meter las communes en la db"""

from app.extensions import db
from app.models.communes import Commune

communes = [
    'Ansignan',
    'Caudiès de Fenouillèdes',
    'Fenouillet',
    'Fosse',
    'Lesquerde',
    'Maury',
    'Prugnanes',
    'Saint Arnac',
    'Saint Martin de Fenouillet',
    'Saint Paul de Fenouillet',
    'Virà'
]

for name in communes:
    db.session.add(Commune(name=name))

db.session.commit()



""" se me olvidó meter las imagenes en la db, lo hacemos ahora con script en flask shell """

from app.models.communes import Commune
from app.extensions import db

images = {
    "Ansignan": "Ansignan.jpg",
    "Caudiès de Fenouillèdes": "Caudiès de Fenouillèdes.png",
    "Fenouillet": "Fenouillet.png",
    "Fosse": "Fosse.png",
    "Lesquerde": "Lesquerde.jpg",
    "Maury": "Maury.png",
    "Prugnanes": "Prugnanes.png",
    "Saint Arnac": "Saint Arnac.png",
    "Saint Martin de Fenouillet": "Saint Martin de Fenouillet.jpg",
    "Saint Paul de Fenouillet": "Saint Paul de Fenouillet.png",
    "Virà": "Virà.png"
}

for commune in Commune.query.all():
    if commune.name in images:
        commune.image = images[commune.name]

db.session.commit()