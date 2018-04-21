from flask import Flask

def create_app(env='dev'):
    app = Flask(__name__)
    app.config.from_object('app.config.config-%s' % env)

    # import blueprints
    from pages.views import pages_app

    # register blueprints
    app.register_blueprint(pages_app)

    if app.debug:
        print 'running in debug mode'
    else:
        print 'NOT running in debug mode'
    return app