# Generated by Django 3.1 on 2020-08-08 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.AlterField(
            model_name='mpesacode',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]