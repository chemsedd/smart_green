# Generated by Django 3.0.6 on 2020-08-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_dashboard', '0004_auto_20200608_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_real_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, db_column='Date')),
                ('temperature', models.IntegerField(db_column='Temperature')),
                ('pressure', models.FloatField(db_column='Pressure')),
                ('humidity', models.FloatField(db_column='Humidity')),
                ('pH', models.FloatField(db_column='pH')),
                ('moisture', models.FloatField(db_column='Moisture')),
            ],
        ),
    ]
