# Generated by Django 4.2.10 on 2024-03-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_notification_email_notification_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
