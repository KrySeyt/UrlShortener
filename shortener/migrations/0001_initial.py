# Generated by Django 4.0.2 on 2022-09-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortedUrl',
            fields=[
                ('full_url', models.URLField()),
                ('key', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
    ]
