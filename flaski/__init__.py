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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)
    
    from . import track
    app.register_blueprint(track.bp)
    app.add_url_rule('/', endpoint='track.index')

    from . import alb
    app.register_blueprint(alb.bp)
    app.add_url_rule('/', endpoint='alb.index')

    from . import art
    app.register_blueprint(art.bp)
    app.add_url_rule('/', endpoint='art.index')

    return app