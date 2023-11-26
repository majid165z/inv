# Generated by Django 3.2.21 on 2023-11-24 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0017_mrsitem_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
