# Generated by Django 5.1.6 on 2025-03-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_account_tryout_tryoutcreator'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='loggedInAs',
            field=models.CharField(default='', max_length=100),
        ),
    ]
