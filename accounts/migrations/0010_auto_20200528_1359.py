# Generated by Django 3.0.6 on 2020-05-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200528_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
