# Generated by Django 3.1 on 2022-07-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20220628_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexpence',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
