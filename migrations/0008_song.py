# Generated by Django 3.2.13 on 2022-04-27 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artist')),
            ],
        ),
    ]
