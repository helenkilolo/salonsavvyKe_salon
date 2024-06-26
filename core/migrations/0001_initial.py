# Generated by Django 4.1.7 on 2024-05-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(choices=[('haircut', 'Haircut'), ('coloring', 'Hair Coloring'), ('styling', 'Hair Styling')], max_length=100)),
            ],
        ),
    ]
