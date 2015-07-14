from django.db import models

# Create your models here.
class ItemTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    create_table_info = models.TextField()
    column_description = models.TextField()
    blood_relation = models.CharField(max_length=200)