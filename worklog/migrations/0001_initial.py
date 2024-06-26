# Generated by Django 5.0.3 on 2024-04-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateWorked', models.DateField()),
                ('HoursWorked', models.FloatField()),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField(null=True)),
                ('break_duration', models.DurationField()),
                ('leave_type', models.CharField(max_length=50)),
                ('leave_duration', models.DurationField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
