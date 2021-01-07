# Generated by Django 3.1.5 on 2021-01-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20210105_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='num_reviews',
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='summary',
            field=models.CharField(default='', max_length=64),
        ),
    ]