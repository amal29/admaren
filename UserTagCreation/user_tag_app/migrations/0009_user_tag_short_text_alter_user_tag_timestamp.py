# Generated by Django 4.0.5 on 2022-06-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tag_app', '0008_remove_user_tag_timestamp1_alter_user_tag_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tag',
            name='short_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_tag',
            name='timestamp',
            field=models.IntegerField(default=1655353803.885525, max_length=200),
        ),
    ]
