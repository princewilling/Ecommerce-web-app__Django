# Generated by Django 4.1.5 on 2023-02-12 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_payment_ref'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_ref',
            new_name='paystack_payment_ref',
        ),
    ]
