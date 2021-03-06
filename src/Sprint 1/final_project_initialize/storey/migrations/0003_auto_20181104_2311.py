# Generated by Django 2.1.1 on 2018-11-04 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storey', '0002_auto_20181104_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('storename', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storey.Retailer')),
            ],
        ),
        migrations.CreateModel(
            name='Shopwebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=40)),
                ('theme', models.IntegerField(default=1)),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storey.Shop')),
            ],
        ),
        migrations.DeleteModel(
            name='HomepageFooter',
        ),
        migrations.AddField(
            model_name='homepage',
            name='website',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storey.Shopwebsite'),
        ),
    ]
