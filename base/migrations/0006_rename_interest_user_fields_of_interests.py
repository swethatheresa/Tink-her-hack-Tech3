# Generated by Django 4.1.2 on 2022-12-17 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='interest',
            new_name='fields_of_interests',
        ),
    ]
