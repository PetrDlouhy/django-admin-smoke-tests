# Generated by Django 4.0.7 on 2022-08-18 13:19

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Channel",
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
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=140, unique=True)),
                ("text", models.TextField(default="")),
                ("rendered_text", models.TextField(blank=True, default="")),
                (
                    "public",
                    models.BooleanField(
                        default=True,
                        help_text="If False, only followers will be able to see content.",
                    ),
                ),
                (
                    "enrollment",
                    models.IntegerField(
                        choices=[(0, "Self"), (1, "Author")], default=0
                    ),
                ),
                ("followers", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="HasPrimarySlug",
            fields=[
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="HasPrimaryUUID",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=140, unique=True)),
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
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=140, unique=True)),
                ("text", models.TextField(default="")),
                ("rendered_text", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("custom_summary", models.TextField(default="")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("published", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.channel"
                    ),
                ),
            ],
            options={
                "ordering": ["published"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ForbiddenPost",
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
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=140, unique=True)),
                ("text", models.TextField(default="")),
                ("rendered_text", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("custom_summary", models.TextField(default="")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("published", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forbidden_posts",
                        to="main.channel",
                    ),
                ),
            ],
            options={
                "ordering": ["published"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FailPost",
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
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=140, unique=True)),
                ("text", models.TextField(default="")),
                ("rendered_text", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("custom_summary", models.TextField(default="")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("published", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.channel"
                    ),
                ),
            ],
            options={
                "ordering": ["published"],
                "abstract": False,
            },
        ),
    ]
