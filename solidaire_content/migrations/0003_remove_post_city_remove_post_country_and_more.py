# Generated by Django 5.1 on 2024-08-23 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solidaire_content', '0002_post_latitude_post_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
        migrations.RemoveField(
            model_name='post',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='post',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='post',
            name='state',
        ),
        migrations.RemoveField(
            model_name='post',
            name='street',
        ),
    ]