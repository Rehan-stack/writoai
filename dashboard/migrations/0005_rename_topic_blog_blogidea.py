# Generated by Django 4.1.3 on 2022-11-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_blog_audience_blog_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='topic',
            new_name='blogIdea',
        ),
    ]
