# Generated by Django 3.2.5 on 2021-09-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]