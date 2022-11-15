# Generated by Django 3.2.16 on 2022-11-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Horse gear', 'horse Equipment'), ('riders gear', 'Riders gear'), ('horse food', 'Horse food'), ('exercise out', 'Exercise'), ('horse care', 'Horse care'), ('selfcare', 'Selfcare')], default='horse care', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_filter',
            field=models.CharField(default='normal', max_length=32),
        ),
    ]