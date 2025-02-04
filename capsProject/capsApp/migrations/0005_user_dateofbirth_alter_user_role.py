# Generated by Django 5.1.4 on 2024-12-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsApp', '0004_user_role_alter_ticket_status_dispute_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dateOfBirth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Police', 'Police'), ('Driver', 'Driver'), ('Admin', 'Admin')], max_length=10),
        ),
    ]
