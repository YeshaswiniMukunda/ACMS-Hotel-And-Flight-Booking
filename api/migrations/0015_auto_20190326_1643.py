# Generated by Django 2.1.7 on 2019-03-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190317_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=14),
            preserve_default=False,
        ),
    ]
