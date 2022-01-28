from app.routes.user_route import user_route

def init_app(app):
    user_route(app)