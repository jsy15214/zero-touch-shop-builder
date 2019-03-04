# Generated by Django 2.1.1 on 2018-11-03 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HomepageHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isVisible', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=40)),
                ('logo', models.ImageField(blank=True, default='storey/default-user-image.png', upload_to='storey')),
                ('logo_height', models.IntegerField(default=40)),
                ('logo_width', models.IntegerField(default=40)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
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
        migrations.AddField(
            model_name='homepage',
            name='website',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storey.Shopwebsite'),
        ),
    ]