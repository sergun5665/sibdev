# Generated by Django 3.0.8 on 2020-07-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200712_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
