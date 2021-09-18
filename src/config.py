import os 

class DevConfig():
    """
    Configuration for local development
    """
    FLASK_APP = "wsgi.py"
    FLASK_ENV = "development"
    DEBUG = True
    # USER = os.environ["POSTGRES_USER"]
    # PASSWORD = os.environ["POSTGRES_PASSWORD"]
    # HOST = os.environ["POSTGRES_HOST"]
    # DATABASE = os.environ["POSTGRES_DB"]
    # PORT = os.environ["POSTGRES_PORT"]
    # DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'