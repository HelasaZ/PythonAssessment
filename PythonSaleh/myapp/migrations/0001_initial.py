# Generated by Django 4.1.7 on 2023-09-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mcom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('flat_booked', models.CharField(max_length=255)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('creation_log', models.DateTimeField()),
                ('booking_value', models.CharField(max_length=255)),
            ],
        ),
    ]