# Generated by Django 3.2.12 on 2023-06-27 13:04

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0032_project_chat_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='chat_file',
            field=models.FileField(blank=True, null=True, upload_to=profiles.models.savenameLocationForChatFiles),
        ),
    ]
