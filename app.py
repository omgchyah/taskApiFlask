import os
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from config import config_by_name
from db import db
from resources.tasks import blp as TasksBlueprint

def create_app(config_name=None):
  app = Flask(__name__) # Create Flask app instance
  
  cfg_name = config_name or os.getenv('FLASK_CONFIG', 'development') # Default to 'development' if not set
  if config_name is None: # If no config_name is provided, use environment variable or default
    config_name = os.getenv('FLASK_ENV', 'development')
  app.config.from_object(config_by_name[cfg_name])
  
  db.init_app(app) # Initialize SQLAlchemy
  migrate = Migrate(app, db) # Initialize Flask-Migrate
  
  api = Api(app) # Initialize Flask-Smorest
  api.register_blueprint(TasksBlueprint) # Register the tasks blueprint
  
  @app.get("/health")
  def health():
    return {"status": "ok"}, 200
  
  return app

# Entry point for running the app
app = create_app()

if __name__ == "__main__":
  app.run()