# Generated by Django 4.0.6 on 2022-07-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_alter_card_date_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='MenuItems/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=10),
        ),
    ]
