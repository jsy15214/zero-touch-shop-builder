# Generated by Django 2.1.1 on 2018-11-28 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storey', '0004_auto_20181128_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shop_name',
            field=models.CharField(default='', max_length=40, null=True),
        ),
    ]