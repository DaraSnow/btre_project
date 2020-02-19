# Generated by Django 3.0.3 on 2020-02-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=3000, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
    ]
