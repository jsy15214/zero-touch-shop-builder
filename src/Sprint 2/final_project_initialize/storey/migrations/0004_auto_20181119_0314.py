# Generated by Django 2.1.1 on 2018-11-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storey', '0003_collectionpagedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpagedetail',
            name='commenting',
            field=models.BooleanField(),
        ),
    ]