# Generated by Django 4.0.5 on 2022-06-15 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tag_app', '0006_alter_user_tag_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tag',
            name='timestamp1',
            field=models.IntegerField(default=1655316968.215956, max_length=200),
        ),
        migrations.AlterField(
            model_name='user_tag',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 23, 46, 8, 215956)),
        ),
    ]
