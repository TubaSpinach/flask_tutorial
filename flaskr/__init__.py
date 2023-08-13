import os

from flask import Flask

def create_app(test_config=None):
    #app factory
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        #then we've got to load it!
        app.config.from_pyfile('config.py',silent=True)
    else:
        #then someone told us where it is
        app.config.from_mapping(test_config)

    #make sure we exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #landing page is Hello world!
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)
    
    return app