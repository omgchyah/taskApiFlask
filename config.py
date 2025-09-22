import os # config.py

class Config:
  API_TITLE = "Task Management API" # Title of the API
  API_VERSION = "v1" # Version of the API
  OPENAPI_VERSION = "3.0.3" # OpenAPI version
  OPENAPI_URL_PREFIX = "/" # URL prefix for OpenAPI
  OPENAPI_SWAGGER_UI_PATH = "/docs" # Path for Swagger UI
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" # URL for Swagger UI assets
  
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///tasks.db") # Default to SQLite if DATABASE_URL is not set
  SQLALCHEMY_TRACK_MODIFICATIONS = False # Disable modification tracking for performance
  
class DevConfig(Config): # Development configuration
  DEBUG = True # Enable debug mode
  
config_by_name = {
  "dev": DevConfig,
  "default": DevConfig,
}
  
  