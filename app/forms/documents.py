

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired



class DocumentForm(FlaskForm):

    title = StringField("Title", validators=[DataRequired()])

    """ separamos por category """
    category = SelectField(
        "Category",
        choices=[
            ("lettre", "Lettre Info"),
            ("deliberation", "Délibérations"),
            ("arrete", "Arrêtés")
        ]
    )

    """ limitamos el tipo de ficheros """
    file = FileField(
        "Document",
        validators=[
            FileAllowed(
                ["pdf", "doc", "docx", "odt", "txt"],
                "Type de fichier non autorisé"
            )
        ]
    )

    file = FileField("PDF")

    submit = SubmitField("Upload")