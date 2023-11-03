# Generated by Django 3.2.21 on 2023-10-30 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_poitem_mr_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrnumber',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mr_numbers', to='warehouse.project', verbose_name='Project'),
            preserve_default=False,
        ),
    ]