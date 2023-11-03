# Generated by Django 3.2.21 on 2023-10-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_remove_poitem_mr_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='poitem',
            name='mr_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poitems', to='warehouse.mrnumber', verbose_name='MR Number'),
        ),
    ]
