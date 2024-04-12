# Generated by Django 5.0.4 on 2024-04-11 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='beers',
        ),
        migrations.AddField(
            model_name='stock',
            name='beer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='stock.beer'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beer',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
