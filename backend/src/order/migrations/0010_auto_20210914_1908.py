# Generated by Django 3.2.5 on 2021-09-14 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210914_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='consignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consignee', to='order.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='consignor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consignor', to='order.customer'),
        ),
    ]
