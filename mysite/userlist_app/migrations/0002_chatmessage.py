# Generated by Django 3.1.4 on 2020-12-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
