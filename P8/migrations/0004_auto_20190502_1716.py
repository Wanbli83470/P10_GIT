# Generated by Django 2.1.7 on 2019-05-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P8', '0003_substitut_user_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='IMG_URL',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='substitut',
            name='IMG_URL',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
