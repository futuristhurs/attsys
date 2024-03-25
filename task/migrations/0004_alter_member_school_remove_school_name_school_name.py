# Generated by Django 5.0.3 on 2024-03-25 01:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_member_school_alter_member_matric_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schools', to='task.school'),
        ),
        migrations.RemoveField(
            model_name='school',
            name='name',
        ),
        migrations.AddField(
            model_name='school',
            name='name',
            field=models.ManyToManyField(max_length=255, related_name='schools', to='task.member'),
        ),
    ]
