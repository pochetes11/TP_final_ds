from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaski.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT '
        ' FROM  JOIN  ON '
        ' ORDER BY  DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


