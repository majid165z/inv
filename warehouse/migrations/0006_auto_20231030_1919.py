# Generated by Django 3.2.21 on 2023-10-30 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('warehouse', '0005_auto_20231029_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='MrNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=40, verbose_name='MR Number')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mr_numbers', to='core.user', verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'شماره MR',
                'verbose_name_plural': 'شماره های MR',
            },
        ),
        
    ]
