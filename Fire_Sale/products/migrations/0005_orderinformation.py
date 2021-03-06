# Generated by Django 4.0.4 on 2022-05-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_seller_alter_productoffer_bidder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('cardholder', models.CharField(max_length=100)),
                ('cardnumber', models.CharField(max_length=19)),
                ('exp', models.CharField(max_length=5)),
                ('cvc', models.CharField(max_length=3)),
            ],
        ),
    ]
