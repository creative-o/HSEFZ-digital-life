# Generated by Django 5.0.2 on 2024-05-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth_league', '0008_appealdata_state_appealdatatest_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appealdata',
            name='creation_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appealdata',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
