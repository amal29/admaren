# Generated by Django 4.0.5 on 2022-06-15 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tag_app', '0005_alter_user_tag_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tag',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 23, 40, 20, 734514)),
        ),
    ]