# Generated by Django 3.1.7 on 2022-08-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_encurta', '0002_auto_20220819_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Public'),
        ),
    ]
