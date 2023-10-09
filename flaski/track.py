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
        """SELECT t.name,a.name FROM tracks t
                JOIN albums al ON al.AlbumId = t.AlbumId
                JOIN artists a ON a.ArtistId = al.ArtistId"""
    ).fetchall()
    return render_template('track/index.html', tracks=tracks)


