# Generated by Django 3.2.4 on 2022-05-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0003_auto_20220503_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allowemail',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='work',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
