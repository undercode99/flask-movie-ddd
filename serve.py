"""
serve.py
- creates an application instance and runs the dev server
"""
from app.application import create_app
app = create_app()
if __name__ == '__main__':
  app.run(host='0.0.0.0')