from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
	kind = models.ManyToManyField('DocType', related_name='docs')
	owner = models.ForeignKey(User, related_name='docs', on_delete=models.CASCADE)
	doc_number = models.CharField(max_length=100, db_index=True)


class DocType(models.Model):
    title = models.CharField(max_length=50, db_index=True)
