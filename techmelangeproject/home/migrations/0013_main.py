# Generated by Django 4.1.1 on 2022-12-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_events_e_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=50)),
                ('mdesc', models.TextField(max_length=1000)),
                ('mdate', models.CharField(max_length=10)),
                ('mbg', models.ImageField(upload_to='')),
            ],
        ),
    ]
