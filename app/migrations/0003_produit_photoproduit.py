# Generated by Django 5.0.1 on 2024-02-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_nomporduit_produit_nomproduit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='photoProduit',
            field=models.ImageField(blank=True, null=True, upload_to='photosProduits/'),
        ),
    ]