from marshmallow import Schema, fields, validate

class TaskCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    description = fields.Str(required=False, validate=validate.Length(max=300), load_default=None)
    location = fields.Str(required=False, validate=validate.Length(max=200), load_default=None)
    due_date = fields.Date(required=False, load_default=None)
    completed = fields.Bool(load_default=False)
    
class TaskUpdateSchema(Schema): # For updating existing tasks
  name = fields.Str(required=False, validate=validate.Length(min=1, max=120))
  description = fields.Str(required=False, validate=validate.Length(max=300), load_default=None)
  location = fields.Str(required=False, validate=validate.Length(max=200), load_default=None)
  due_date = fields.DateTime(required=False, load_default=None)
  completed = fields.Bool(required=False)
  
class TaskOutputSchema(Schema): # For outputting task data
  id = fields.Int(dump_only=True)
  name = fields.Str()
  description = fields.Str(allow_none=True)
  location = fields.Str(allow_none=True)
  due_date = fields.DateTime(allow_none=True)
  created_at = fields.DateTime()
  updated_at = fields.DateTime()
  completed = fields.Bool()
  deleted = fields.Bool()
  