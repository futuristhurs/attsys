# Generated by Django 5.0.3 on 2024-03-25 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_member_school_remove_school_name_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school', to='task.school'),
        ),
        migrations.RemoveField(
            model_name='school',
            name='name',
        ),
        migrations.AddField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
