from datetime import datetime
from datetime import timezone
from db import db

class Task(db.Model):
  __tablename__ = 'tasks' # Table name in the database
  
  id = db.Column(db.Integer, primary_key=True) # Primary key
  name = db.Column(db.String(120), unique=True, nullable=False) # Task name
  description = db.Column(db.String(300), nullable=True)
  location = db.Column(db.String(200), nullable=True)
  due_date = db.Column(db.Date, nullable=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Timestamp of creation
  updated_at = db.Column(
    db.DateTime,
    nullable=False,
    default=datetime.utcnow,
    onupdate=datetime.utcnow
  )
  
  #statuses
  completed = db.Column(db.Boolean, nullable=False, default=False)
  deleted = db.Column(db.Boolean, nullable=False, default=False)
  
  def __repr__(self) -> str:
    return (
            f"<Task id={self.id} name={self.name!r} "
            f"description={self.description!r} completed={self.completed} deleted={self.deleted}>"
        )
  