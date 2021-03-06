# Generated by Django 3.2.12 on 2022-05-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220510_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(db_index=True, max_length=500, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=50, verbose_name='User Name'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
