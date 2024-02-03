# Generated by Django 4.1.7 on 2023-10-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_Portal', '0010_alter_transaction_reciver_alter_transaction_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('mission_statement', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('bank_account_number', models.CharField(max_length=30)),
                ('social_media_links', models.URLField(blank=True, null=True)),
                ('registration_proof', models.ImageField(upload_to='registration_proofs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]