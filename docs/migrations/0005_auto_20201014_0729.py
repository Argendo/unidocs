# Generated by Django 3.1.2 on 2020-10-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20201014_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_number',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
