# Generated by Django 5.0.2 on 2024-05-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth_league', '0010_alter_appealdatatest_creation_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appealdata',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appealdata',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appealdatatest',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appealdatatest',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
