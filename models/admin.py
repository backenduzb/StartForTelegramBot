from tortoise import Model, fields

class Admin(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=640)
    tg_id = fields.BigIntField()
    