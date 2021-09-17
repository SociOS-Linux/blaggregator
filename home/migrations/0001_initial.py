# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-02 04:10


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("feed_url", models.URLField()),
                (
                    "last_crawled",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name=b"last crawled"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name=b"date created"
                    ),
                ),
                (
                    "stream",
                    models.CharField(
                        choices=[(b"BLOGGING", b"blogging"), (b"LOGS", b"Daily Logs")],
                        default=b"BLOGGING",
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hacker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("avatar_url", models.TextField(blank=True)),
                ("github", models.TextField(blank=True)),
                ("twitter", models.TextField(blank=True)),
                (
                    "token",
                    models.SlugField(
                        default=home.models.token_default, max_length=40, unique=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LogEntry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("referer", models.URLField(blank=True, null=True)),
                ("remote_addr", models.GenericIPAddressField(blank=True, null=True)),
                ("user_agent", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.TextField()),
                ("title", models.TextField(blank=True)),
                ("content", models.TextField()),
                (
                    "date_posted_or_crawled",
                    models.DateTimeField(verbose_name=b"date updated"),
                ),
                (
                    "slug",
                    models.CharField(
                        default=home.models.generate_random_id,
                        max_length=6,
                        unique=True,
                    ),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.Blog"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="logentry",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.Post"
            ),
        ),
    ]
