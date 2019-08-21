# Generated by Django 2.0.2 on 2018-04-04 16:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distname', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
                'ordering': ('distname',),
            },
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ('county_nam',), 'verbose_name': 'county', 'verbose_name_plural': 'counties'},
        ),
        migrations.AddField(
            model_name='county',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='county',
            name='county_nam',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='land.District'),
        ),
    ]