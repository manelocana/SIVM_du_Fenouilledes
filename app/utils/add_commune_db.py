

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