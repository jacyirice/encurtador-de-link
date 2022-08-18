# Generated by Django 3.1.7 on 2022-08-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255, verbose_name='Link')),
                ('link_short', models.URLField(unique=True, verbose_name='Link short')),
            ],
        ),
    ]
