# Generated by Django 2.2.28 on 2024-09-26 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20240922_0215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['creatade_date']},
        ),
    ]
