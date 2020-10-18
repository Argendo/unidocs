# Generated by Django 3.1.2 on 2020-10-16 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0011_auto_20201016_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='doc_type',
        ),
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
