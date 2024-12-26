import os
from dotenv import load_dotenv
from flask.cli import FlaskGroup
from project import create_app

load_dotenv()

app=create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    app.run(port=5001)
    cli()