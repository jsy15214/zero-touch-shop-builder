# Generated by Django 2.1.1 on 2018-11-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storey', '0006_merge_20181128_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagenavbar',
            name='text',
            field=models.CharField(default='My Website', max_length=40),
        ),
        migrations.AlterField(
            model_name='homepageproductdemo',
            name='description_1',
            field=models.CharField(default="When you use a theme created by Start Bootstrap,\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t you know that the theme will look great on any device, \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t whether it's a phone, tablet, or desktop the page will \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t behave responsively!", max_length=300),
        ),
        migrations.AlterField(
            model_name='homepageproductdemo',
            name='description_2',
            field=models.CharField(default='Newly improved, and full of great utility classes, Bootstrap 4\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t is leading the way in mobile responsive web development! All of \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t the themes on Start Bootstrap are now using Bootstrap 4!', max_length=300),
        ),
        migrations.AlterField(
            model_name='homepageproductdemo',
            name='name_1',
            field=models.CharField(default='Fully Responsive Design', max_length=40),
        ),
        migrations.AlterField(
            model_name='homepageproductdemo',
            name='name_2',
            field=models.CharField(default='Updated For Bootstrap4', max_length=40),
        ),
    ]
