from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaski.db import get_db

bp = Blueprint('track', __name__, url_prefix="/track")

@bp.route('/')
def index():
    db = get_db()
    tracks = db.execute(
        """SELECT t.name AS canciones, g.name AS genero, ar.name AS artista, mt.name AS formato, a.title AS titulo
                FROM tracks t JOIN albums a ON t.AlbumId = a.AlbumId
                JOIN genres g ON g.GenreId = t.GenreId 
                JOIN artists ar ON ar.ArtistId = a.ArtistId
                JOIN media_types mt ON mt.MediaTypeId = t.MediaTypeId
                ORDER BY t.name DESC"""
    ).fetchall()
    return render_template('track/index.html', tracks=tracks)


