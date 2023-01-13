# Generated by Django 3.2.12 on 2023-01-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_work_show_in_top_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='artist',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='artistrequest',
            name='skill',
        ),
        migrations.AddField(
            model_name='artist',
            name='skill',
            field=models.ManyToManyField(blank=True, default='', to='profiles.Skill'),
        ),
        migrations.AddField(
            model_name='artistrequest',
            name='skill',
            field=models.ManyToManyField(blank=True, default='', related_name='artistrequest_Skill', to='profiles.Skill'),
        ),
    ]
