# Generated by Django 3.2.13 on 2022-04-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220427_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.CharField(blank=True, db_column='age1', max_length=100, null=True),
        ),
    ]