# Generated by Django 5.0.4 on 2024-04-12 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='beer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stock.beer'),
        ),
    ]
