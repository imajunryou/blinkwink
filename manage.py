# manage.py

import os

from blinkwink import create_app

from flask_script import Manager

# Either the config level is set in an environment variable
# or we just use the development version of the config
app = create_app(os.getenv("BLINKWINK_ENV") or "dev")
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
