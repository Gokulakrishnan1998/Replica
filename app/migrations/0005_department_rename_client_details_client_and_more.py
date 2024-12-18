# Generated by Django 5.1.1 on 2024-11-24 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_employee_details_dept_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=30)),
                ('manager_id', models.IntegerField(null=True)),
                ('dept_location', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='client_details',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='signup_details',
            new_name='Signup',
        ),
        migrations.RenameModel(
            old_name='employee_details',
            new_name='Employee',
        ),
        migrations.RenameModel(
            old_name='project_details',
            new_name='Project',
        ),
        migrations.AlterField(
            model_name='employee',
            name='dept_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.department'),
        ),
        migrations.AlterField(
            model_name='project',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department'),
        ),
        migrations.DeleteModel(
            name='department_details',
        ),
    ]
