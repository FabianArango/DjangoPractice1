# Generated by Django 3.1.7 on 2021-04-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210412_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilePic',
            field=models.FileField(default='static/upload/profilePic/default.gif', upload_to='static/upload/profilePic/'),
        ),
    ]