# Generated by Django 4.2.3 on 2023-08-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0011_alter_room_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="size",
            field=models.IntegerField(),
        ),
    ]
