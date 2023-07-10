# Generated by Django 3.2.5 on 2021-11-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-dateCreated']},
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(blank=True, default='{latitude: 10.0171277, longitude: 105.7842959}', max_length=100, null=True),
        ),
    ]
