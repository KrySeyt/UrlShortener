# Generated by Django 4.0.2 on 2022-09-11 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_rename_shortedurl_url_rename_key_url_short_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_url',
            new_name='short_url_key',
        ),
    ]