# Generated by Django 4.2.16 on 2024-11-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_updated_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
