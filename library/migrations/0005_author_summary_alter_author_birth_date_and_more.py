# Generated by Django 4.2.7 on 2023-11-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_author_photo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='summary',
            field=models.TextField(default=0, max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(default=' '),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(default=' '),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_pages',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(default='', max_length=800),
        ),
    ]
