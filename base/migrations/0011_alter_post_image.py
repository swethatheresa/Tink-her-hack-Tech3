# Generated by Django 4.1.2 on 2022-12-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
