# Generated by Django 2.1.15 on 2020-04-21 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='user',
        ),
    ]
