# Generated by Django 3.1 on 2020-08-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_album_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.CharField(default='0000', max_length=5),
        ),
    ]
