from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    gender = fields.CharField(max_length=10)
    status = fields.CharField(max_length=10)


class Post(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="posts")
    title = fields.CharField(max_length=200)
    body = fields.TextField()
