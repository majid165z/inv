# Generated by Django 3.2.21 on 2023-10-29 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_materialreceiptsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='MRSItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Quantity')),
                ('loc', models.CharField(blank=True, max_length=10, null=True, verbose_name='loc')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('condition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mrsitems', to='warehouse.condition', verbose_name='Condition')),
                ('mrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='warehouse.materialreceiptsheet')),
                ('pl_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mrsitems', to='warehouse.plitem', verbose_name='PO Item Num')),
            ],
            options={
                'verbose_name': 'MRS Item',
                'verbose_name_plural': 'MRS Items',
            },
        ),
        migrations.CreateModel(
            name='inventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoming', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='incoming')),
                ('outgoing', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='outgoing')),
                ('remaining', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='remaining')),
                ('total_in_all_warehouse_project', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='total_in_all_warehouse_project')),
                ('total_in_all', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='total_in_all')),
                ('condition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ivitems', to='warehouse.condition', verbose_name='Condition')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivitems', to='warehouse.item', verbose_name='Item Description')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ivitems', to='warehouse.project', verbose_name='Project')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivitems', to='warehouse.warehouse', verbose_name='Warehouse')),
            ],
            options={
                'verbose_name': 'inventory Item',
                'verbose_name_plural': 'inventory Item',
            },
        ),
    ]
