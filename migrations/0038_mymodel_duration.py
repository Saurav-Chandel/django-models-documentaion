# Generated by Django 3.2.13 on 2022-05-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_rename_album_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='duration',
            field=models.DurationField(default=1),
            preserve_default=False,
        ),
    ]