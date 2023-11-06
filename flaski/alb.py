from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaski.db import get_db

bp = Blueprint('alb', __name__, url_prefix="/album")

@bp.route('/')
def index():
    db = get_db()
    album = db.execute(
        '''SELECT t.name AS canciones, title AS dvd, ar.name AS artista, g.name AS genero
         FROM tracks t JOIN albums a ON t.albumId = a.albumId
         JOIN artists ar ON ar.ArtistId = a.ArtistId
         JOIN genres g ON g.GenreId = t.GenreId
         ORDER BY t.name DESC'''
    ).fetchall()
    return render_template('album/index.html', album=album)


