# Generated by Django 4.2.7 on 2023-12-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
