# Generated by Django 4.1.1 on 2022-12-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_teachcoor_delete_teach_coor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='aboutp',
        ),
        migrations.AddField(
            model_name='sponsers',
            name='spon_logo',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='pics/'),
        ),
    ]
