# Generated by Django 4.2.5 on 2023-09-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]