# Generated by Django 4.2.16 on 2024-11-24 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0005_contact_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="name",
        ),
    ]
