# Generated by Django 3.2.21 on 2023-11-16 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0014_remove_miritem_pl_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='miritem',
            name='mrs_item',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='miritems', to='warehouse.mrsitem', verbose_name='PO Item Num'),
            preserve_default=False,
        ),
    ]
