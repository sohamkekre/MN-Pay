# Generated by Django 4.1.7 on 2023-11-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0040_alter_transaction_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='receiver',
            field=models.CharField(max_length=30),
        ),
    ]
