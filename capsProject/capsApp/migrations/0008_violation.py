# Generated by Django 5.1.4 on 2025-01-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsApp', '0007_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('penalty_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
