# Generated by Django 3.2.13 on 2022-04-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_rename_id_mymodel_roll_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]