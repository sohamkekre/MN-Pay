# Generated by Django 4.1.7 on 2023-11-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0039_country_country_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.CharField(max_length=30),
        ),
    ]