# Generated by Django 2.1.1 on 2019-02-05 19:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('street', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='widgets.PointField')),
            ],
        ),
    ]
