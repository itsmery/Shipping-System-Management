# Generated by Django 3.2.5 on 2021-09-14 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0008_consignee_consignor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('cnor', 'Consignor'), ('cnee', 'Consignee')], max_length=25)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('provinceId', models.IntegerField(blank=True, null=True)),
                ('districtId', models.IntegerField(blank=True, null=True)),
                ('subDistrictId', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='consignor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Consignee',
        ),
        migrations.DeleteModel(
            name='Consignor',
        ),
    ]
