"""
migrate.py
- create and update database
"""
from app.infrastructure.persistence.sqlalchemy.models import auto_create_table

if __name__ == '__main__':
    auto_create_table()
