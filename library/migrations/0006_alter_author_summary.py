# Generated by Django 4.2.7 on 2023-11-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_author_summary_alter_author_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='summary',
            field=models.TextField(default=' ', max_length=800),
        ),
    ]
