import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaski.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says tuki
    @app.route('/tuki')
    def tuki():
        return 'tuki!'
    
    @app.route('/')
    def index():
        return render_template('index.html')

    from . import auth
    app.register_blueprint(auth.bp) 
    
    from . import db
    db.init_app(app)


    #from . import auth
    #app.register_blueprint(auth.bp)
    
    from . import track
    app.register_blueprint(track.bp)
    app.register_blueprint(track.bpapi)

    from . import albums
    app.register_blueprint(albums.bp)
    app.register_blueprint(albums.bpapi)

    from . import artist
    app.register_blueprint(artist.bp)
    app.register_blueprint(artist.bpapi)
    
    return app