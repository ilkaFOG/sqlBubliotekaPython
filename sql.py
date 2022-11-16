from peewee import *


class BooksModel(Model):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100)
    year = IntegerField()
    author = CharField(max_length=100)

    class Meta:
        db_table = "Library"
        order_by = ("id",)