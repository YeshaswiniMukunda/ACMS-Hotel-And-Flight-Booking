# Generated by Django 2.1.7 on 2019-04-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20190405_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight_seats',
            name='id',
            field=models.AutoField(help_text='Unique ID for this particular seat', primary_key=True, serialize=False),
        ),
    ]