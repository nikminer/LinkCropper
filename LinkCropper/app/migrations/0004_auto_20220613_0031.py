# Generated by Django 2.2.28 on 2022-06-12 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220613_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterFolder',
            fields=[
                ('folder', models.TextField(primary_key=True, serialize=False)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReddirectId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.TextField()),
                ('linkid', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='reddirectusertable',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.ReddirectId'),
        ),
    ]
