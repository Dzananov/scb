# Generated by Django 3.2.16 on 2023-01-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='.../default_profile_mzoqgl', upload_to='images/'),
        ),
    ]