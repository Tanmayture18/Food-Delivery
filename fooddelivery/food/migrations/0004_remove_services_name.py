# Generated by Django 3.2.6 on 2022-03-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_services_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='name',
        ),
    ]
