# Generated by Django 3.0.4 on 2020-04-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200415_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(upload_to='', verbose_name='carrier.png'),
        ),
    ]
