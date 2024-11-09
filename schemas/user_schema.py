# schemas/user_schema.py
user_schema = {
    "username": {"type": "string", "required": True},
    "email": {"type": "string", "required": True},
    "age": {"type": "integer", "required": False}
}