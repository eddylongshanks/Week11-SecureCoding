# Generated by Django 3.1.4 on 2020-12-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=80)),
                ('secondname', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=32)),
            ],
        ),
    ]
