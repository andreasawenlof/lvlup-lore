# Generated by Django 4.2.16 on 2024-11-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_contact_created_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="subject",
            field=models.CharField(default="Yesss", max_length=100),
            preserve_default=False,
        ),
    ]
