# Generated by Django 5.1.7 on 2025-04-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_account_unique_together_remove_account_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='checkout_phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Checkout phone number'),
        ),
    ]
