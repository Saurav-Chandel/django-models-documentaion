# Generated by Django 3.2.13 on 2022-04-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_artist_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='id',
        ),
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.CharField(blank=True, db_column='age1', max_length=100, primary_key=True, serialize=False),
        ),
    ]
