# Generated by Django 4.1.7 on 2023-09-30 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0002_customer_delete_usersignup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zipcode',
            new_name='ac_number',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='city',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.AddField(
            model_name='customer',
            name='ifsc_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=11),
            preserve_default=False,
        ),
    ]
