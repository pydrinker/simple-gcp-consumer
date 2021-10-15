from pydrinker.managers import DrinkerManager

from .routes import routes

manager = DrinkerManager(routes=routes)
manager.run()
