# Generated by Django 3.1.2 on 2020-10-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_document_doc_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='kind',
        ),
        migrations.DeleteModel(
            name='DocType',
        ),
    ]
