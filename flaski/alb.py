rom flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaski.db import get_db

bp = Blueprint('alb', __name__, url_prefix="/album")

@bp.route('/')
def index():
    db = get_db()
    album = db.execute(
        """SELECT t.name as titulo,al.Title as cancion FROM tracks t
                JOIN albums al ON al.AlbumId = t.AlbumId
                JOIN artists a ON a.ArtistId = al.ArtistId"""
    ).fetchall()
    return render_template('album/index.html', album=album)


