# Generated by Django 4.0.6 on 2022-08-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chararacter',
            name='limit',
            field=models.CharField(default=True, editable=False, max_length=3),
        ),
    ]