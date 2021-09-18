import os 
from src.app import create_app

env = os.environ["FLASK_ENV"]
app = create_app(env)

# TODO - add logging here 

if __name__ == "__main__":
    try: 
        app.run(host="0.0.0.0", port=8080)
    except Exception as err: 
        raise err 