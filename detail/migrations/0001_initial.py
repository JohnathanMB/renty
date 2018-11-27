# Generated by Django 2.1.3 on 2018-11-20 20:06

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=2083)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('pickup', models.CharField(default='Aeropuerto', max_length=100)),
                ('plate', models.IntegerField()),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('capacity', models.IntegerField(default=1)),
                ('transmission', models.CharField(default='Mecanica', max_length=20)),
                ('doors', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('color', models.CharField(max_length=20)),
                ('kms', models.IntegerField(default=0)),
                ('pictures', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2083), blank=True, size=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Rental'),
        ),
    ]
