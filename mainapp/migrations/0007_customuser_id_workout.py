# Generated by Django 5.1.2 on 2024-12-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_json_field_usertraining_json_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='id_workout',
            field=models.IntegerField(null=True),
        ),
    ]