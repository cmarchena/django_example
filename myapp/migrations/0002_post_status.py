# Generated by Django 5.0.6 on 2024-06-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.TextField(default="draft"),
        ),
    ]
