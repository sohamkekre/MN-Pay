# Generated by Django 4.1.7 on 2023-11-03 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0044_alter_ngo_contact_person_alter_ngo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='created_at',
        ),
    ]
