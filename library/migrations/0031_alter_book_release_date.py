# Generated by Django 4.2.7 on 2023-11-21 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0030_alter_book_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
