# manage.py

from flask_script import Manager

from main import app

manager = Manager(app)

@manager.command
def hello():
    print("Hello")

if __name__ == "__main__":
    manager.run()
