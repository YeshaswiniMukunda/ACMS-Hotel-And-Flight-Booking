# Generated by Django 2.1.5 on 2019-03-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190316_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomavailability',
            name='status',
            field=models.CharField(choices=[('bk', 'Booked'), ('pr', 'Processing'), ('dd', 'Dead')], help_text='Status', max_length=2),
        ),
    ]
