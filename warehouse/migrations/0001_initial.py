# Generated by Django 3.2.21 on 2023-10-27 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clusters', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'Cluster',
                'verbose_name_plural': 'Clusters',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Item Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
        ),
        migrations.CreateModel(
            name='PipeLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pipelines', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'Pipe Line',
                'verbose_name_plural': 'Pipe Lines',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouses', to='core.user', verbose_name='Created By')),
                ('users', models.ManyToManyField(blank=True, limit_choices_to={'warehouse_keeper': True}, related_name='whs', to='core.User', verbose_name='Warehouse Keepers')),
            ],
            options={
                'verbose_name': 'انبار',
                'verbose_name_plural': 'انبارها',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Unit Name')),
                ('abrv', models.CharField(max_length=10, verbose_name='Abriviation')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='core.user', verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'واحد',
                'verbose_name_plural': 'واحد ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Project Name')),
                ('number', models.CharField(max_length=40, verbose_name='Project Number')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='core.user', verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='ProcurementOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='PO Number')),
                ('date', models.DateField(blank=True, verbose_name='Date Confirmed')),
                ('company', models.CharField(max_length=100, verbose_name='Seller (Company Name)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pos', to='core.user', verbose_name='ثبت شده توسط')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pos', to='warehouse.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'سفارش خرید',
                'verbose_name_plural': 'سفارش های خرید',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='POItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Mr Item No.')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Quantity')),
                ('mr_number', models.CharField(max_length=200, verbose_name='MR Number')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poitems', to='warehouse.cluster', verbose_name='cluster')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poitems', to='warehouse.item', verbose_name='Item Description')),
                ('pipeline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poitems', to='warehouse.pipeline', verbose_name='pipe line')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='warehouse.procurementorder')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poitems', to='warehouse.unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'قلم سفارش خرید',
                'verbose_name_plural': 'اقلام سفارش خرید',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Condition')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conditions', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'Condition',
                'verbose_name_plural': 'Conditions',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
