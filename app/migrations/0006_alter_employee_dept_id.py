# Generated by Django 5.1.1 on 2024-11-24 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_department_rename_client_details_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.department'),
        ),
    ]
