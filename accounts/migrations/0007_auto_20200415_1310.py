# Generated by Django 3.0.4 on 2020-04-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200415_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='carrier.png', upload_to=''),
        ),
    ]
