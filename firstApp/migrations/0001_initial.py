# Generated by Django 4.1.5 on 2023-01-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
