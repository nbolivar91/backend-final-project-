# Generated by Django 2.1.1 on 2019-02-01 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190201_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderentity',
            name='ciudad',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coders', to='api.CiudadEntity'),
        ),
    ]
