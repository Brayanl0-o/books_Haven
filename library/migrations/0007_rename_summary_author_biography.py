# Generated by Django 4.2.7 on 2023-11-27 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_author_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='summary',
            new_name='biography',
        ),
    ]