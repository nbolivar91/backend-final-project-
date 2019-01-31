# Generated by Django 2.1.5 on 2019-01-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190130_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='coderentity',
            name='biografia',
            field=models.CharField(default=None, max_length=1000000000, null=True),
        ),
        migrations.AddField(
            model_name='coderentity',
            name='cedula',
            field=models.IntegerField(default=None, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='coderentity',
            name='costoXhora',
            field=models.FloatField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coderentity',
            name='experiencia',
            field=models.IntegerField(default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='coderentity',
            name='email',
            field=models.EmailField(default=None, max_length=250, null=True),
        ),
    ]