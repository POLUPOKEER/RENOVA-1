# Generated by Django 5.1.2 on 2024-12-08 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_usertraining_json_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertraining',
            old_name='json_field',
            new_name='json_data',
        ),
    ]
