# Generated by Django 3.1 on 2022-07-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0004_auto_20220705_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addincome',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
