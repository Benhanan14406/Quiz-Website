# Generated by Django 5.1.6 on 2025-03-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_tryouts_tryout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tryout',
            old_name='tryoutDescp',
            new_name='tryoutDesc',
        ),
        migrations.AlterField(
            model_name='tryout',
            name='tryoutNums',
            field=models.IntegerField(),
        ),
    ]
