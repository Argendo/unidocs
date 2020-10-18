# Generated by Django 3.1.2 on 2020-10-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0010_remove_document_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(max_length=150, null='kek', unique=True),
            preserve_default='kek',
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]