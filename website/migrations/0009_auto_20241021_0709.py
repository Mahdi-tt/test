# Generated by Django 2.2.28 on 2024-10-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20241021_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]