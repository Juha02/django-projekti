# Generated by Django 3.2.7 on 2021-09-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kauppa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuote',
            name='hinta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
