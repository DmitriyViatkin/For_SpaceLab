from tortoise.models import Model
from tortoise import fields

class User(Model):
    
    user_id=fields.IntField(primary_key=True)
    name=fields.CharField(max_lengxt=50)
    email=fields.CharField(max_lenght=70, unique=True)
    gender=fields.CharField(max_lenght=20)
    status=fields.CharField(max_lenght=10)

class Post(Model):
    
    id_post=fields.IntField(primary_key=True)
    user_id=fields.ForeignKeyField("model.User", related_name="Posts")
    title=fields.CharField(max_lengxt=200)
    body=fields.TextField()