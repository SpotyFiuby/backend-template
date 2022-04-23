# import models.py from app.database.models
# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from ..models.users import Users
