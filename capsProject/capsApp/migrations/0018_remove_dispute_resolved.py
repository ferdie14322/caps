# Generated by Django 5.1.4 on 2025-01-02 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capsApp', '0017_alter_ticket_issued_by_alter_ticket_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispute',
            name='resolved',
        ),
    ]
