# Generated by Django 4.2.3 on 2023-07-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travllo2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
