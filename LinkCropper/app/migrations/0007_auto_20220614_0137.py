# Generated by Django 2.2.28 on 2022-06-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220613_0126'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reddirectid',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='reddirectuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='reddirectuser',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
