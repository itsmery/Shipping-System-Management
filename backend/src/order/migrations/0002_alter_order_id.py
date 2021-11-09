# Generated by Django 3.2.5 on 2021-11-08 10:26

from django.db import migrations, models
import order.utils


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(default=order.utils.customOrderId, max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]