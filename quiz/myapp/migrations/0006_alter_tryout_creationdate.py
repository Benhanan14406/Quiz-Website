# Generated by Django 5.1.6 on 2025-03-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_category_tryout_tryoutcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tryout',
            name='creationDate',
            field=models.DateField(default='', editable=False, max_length=100),
        ),
    ]
