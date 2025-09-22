from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

from db import db
from models import Task
from schemas import TaskCreateSchema, TaskUpdateSchema, TaskOutputSchema

blp = Blueprint("Tasks", __name__, description="CRUD on tasks")

@blp.route("/tasks")
class TasksList(MethodView):
  @blp.response(200, TaskOutputSchema(many=True))
  def get(self):
    """Get all non-deleted tasks"""
    tasks = Task.query.filter_by(deleted=False).order_by(Task.id.desc()).all()
    return tasks

  @blp.arguments(TaskCreateSchema)
  @blp.response(201, TaskOutputSchema)
  def post(self, new_data):
    """Create a new task"""
    new_task = Task(**new_data)
    db.session.add(new_task)
    try:
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      abort(400, message="Task with this name already exists.")
    return new_task
  
@blp.route("/tasks/<int:task_id>")
class TaskItem(MethodView):
  
  @blp.response(200, TaskOutputSchema) # For outputting task data
  def get(self, task_id):
    """Get a specific task by id"""
    task = Task.query.get_or_404(task_id)
    if task.deleted:
      abort(404, message="Task not found.")
    return task
  
  #Partial update of a task
  @blp.arguments(TaskUpdateSchema)
  @blp.response(200, TaskOutputSchema)
  def patch(self, update_data, task_id):
    task = Task.query.get_or_404(task_id)
    if task.deleted:
      abort(404, message="Task not found.")
      for k, v in up_data.items():
        setattr(task, k, v)
      try:
        db.session.commit()
      except IntegrityError: # Handle unique constraint violation
        db.session.rollback()
        abort(400, message="Task with this name already exists.")
      return task
      
  @blp.response(204)
  def delete(self, task_id):
    """Soft delete a task by setting its deleted status to True"""
    task = Task.query.get_or_404(task_id)
    if not task.deleted:
      task.deleted = True
      db.session.commit()
      return "", 204
    abort(404, message="Task not found.")
  
        
    
        
  