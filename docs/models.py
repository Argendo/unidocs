from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from django.utils.text import slugify
from time import time

def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-'+str(int(time()))

class Document(models.Model):
	doc_number = models.CharField(max_length=100)
	doc_type = models.ForeignKey('DocType', related_name='docs', on_delete= models.CASCADE, null=True)
	owner = models.ForeignKey(User, related_name='docs', on_delete= models.CASCADE, null=True)
	slug = models.SlugField(max_length=150, blank=True, unique=True)

	def __str__(self):
		return self.doc_number

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.doc_number)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('doc_detail_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('doc_delete_url', kwargs={'slug': self.slug})

class DocType(models.Model):
	title = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.title