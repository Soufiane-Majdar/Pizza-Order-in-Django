# Generated by Django 4.0.6 on 2022-07-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(choices=[(1, 'Rabat'), (2, 'Kenitra'), (3, 'Tanger'), (4, 'Oriental'), (5, 'Souss'), (6, 'Fes'), (7, 'Marrakech'), (8, 'Meknes'), (9, 'Agadir'), (10, 'Tetouan'), (11, 'Safi'), (12, 'Settat'), (13, 'Khouribga'), (14, 'Sale'), (15, 'Oujda'), (16, 'Taza'), (17, 'Tiznit')], default='Kenitra', max_length=50),
        ),
    ]
