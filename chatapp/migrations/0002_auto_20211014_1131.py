# Generated by Django 3.2.7 on 2021-10-14 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fileupload',
        ),
        migrations.RemoveField(
            model_name='message',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='file_status',
        ),
    ]