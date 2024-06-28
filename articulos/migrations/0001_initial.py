# Generated by Django 4.1.5 on 2024-06-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("contenido", models.TextField(max_length=100)),
                ("categoria", models.CharField(max_length=50)),
                ("creado", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]