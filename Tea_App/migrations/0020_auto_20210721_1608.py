# Generated by Django 3.2 on 2021-07-21 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0019_auto_20210721_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteutilities',
            old_name='description',
            new_name='disclaimer',
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 16, 8, 7, 291902)),
        ),
    ]
