from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

#from application.auth import login_required
from application.db import get_db

bp = Blueprint('albums', __name__, url_prefix='/album')
bpapi = Blueprint('api_album', __name__, url_prefix="/api/album")

@bp.route('/')
def index():
    db = get_db()
    db.execute(
        """SELECT AlbumId AS id, Title AS album 
         FROM albums
         ORDER BY Title DESC """
    )
    albums = db.fetchall()
    return render_template('albums/index.html', albums=albums)
@bp.route('/<int:id>/', methods=('GET', 'POST'))
def get_album(id):
    db = get_db()
    db.execute(
    """SELECT AlbumId AS id, Title AS album 
         FROM albums
          """
    )
    album = db.fetchone()

    db.execute(
        """SELECT t.Name AS nombre, g.Name AS genero, Composer, Milliseconds,
         Bytes, UnitPrice
         FROM tracks t 
         JOIN genres g ON t.GenreId=g.GenreId
         JOIN albums a ON t.AlbumId=a.AlbumId
         WHERE t.AlbumId = %s
         """,
        (id,)
    )
    tracksi = db.fetchall()

    if album is None:
        abort(404, f"Album id {id} doesn't exist.")

    return render_template('albums/detalles.html', album=album, tracksi=tracksi)

@bpapi.route('/')
def index():
    db = get_db()
    db.execute(
        """SELECT AlbumId AS id, Title AS album 
         FROM albums
         ORDER BY Title DESC """
    )
    albums = db.fetchall()
    return jsonify(albums=albums)

@bpapi.route('/<int:id>/', methods=('GET', 'POST'))
def get_album(id):
    db = get_db()
    db.execute(
    """SELECT AlbumId AS id, Title AS album 
         FROM albums
          """
    )
    album = db.fetchall()
    db.execute(
        """SELECT t.Name AS nombre, g.Name AS genero, Composer, Milliseconds,
         Bytes, UnitPrice
         FROM tracks t 
         JOIN genres g ON t.GenreId=g.GenreId
         JOIN albums a ON t.AlbumId=a.AlbumId
         WHERE t.AlbumId = %s
         """,
        (id,)
    )
    tracksi =db.fetchall()

    if album is None:
        abort(404, f"Album id {id} doesn't exist.")

    return jsonify(album=album, tracksi=tracksi)


