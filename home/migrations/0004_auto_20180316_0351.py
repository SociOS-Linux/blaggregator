# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 07:51


from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20180313_1026"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="date_posted_or_crawled",
            new_name="created_at",
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name=b"creation timestamp"
            ),
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]
