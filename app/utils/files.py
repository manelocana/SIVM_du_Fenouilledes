


import os
import uuid
from flask import current_app





def save_file(file, folder):

    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"

    upload_path = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        folder
    )

    os.makedirs(upload_path, exist_ok=True)

    file_path = os.path.join(upload_path, filename)

    file.save(file_path)

    return filename





def delete_file(filename, folder):

    path = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        folder,
        filename
    )

    if os.path.exists(path):
        os.remove(path)