# Generated by Django 3.2.21 on 2023-10-27 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='Packing List Number')),
                ('company', models.CharField(max_length=100, verbose_name='شرکت فروشنده کالا')),
                ('date', models.DateField(blank=True, verbose_name='Sent Date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pls', to='core.user', verbose_name='ثبت شده توسط')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pls', to='warehouse.procurementorder', verbose_name='PO Number')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pls', to='warehouse.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'بارنامه',
                'verbose_name_plural': 'بارنامه ها',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='cluster',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='poitem',
            name='number',
            field=models.PositiveIntegerField(verbose_name='PO Item No.'),
        ),
        migrations.CreateModel(
            name='PLItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Quantity')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='warehouse.packinglist')),
                ('po_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plitems', to='warehouse.poitem', verbose_name='PO Item No.')),
            ],
            options={
                'verbose_name': 'قلم  بارنامه',
                'verbose_name_plural': 'اقلام بارنامه',
            },
        ),
    ]