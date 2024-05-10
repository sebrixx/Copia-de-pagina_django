# Generated by Django 4.2.1 on 2023-06-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=20000)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]
