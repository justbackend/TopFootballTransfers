# Generated by Django 4.2.5 on 2023-09-27 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('logo', models.FileField(upload_to='')),
                ('davlat', models.CharField(max_length=50)),
                ('prezident', models.CharField(blank=True, max_length=50, null=True)),
                ('murabbiy', models.CharField(blank=True, max_length=50, null=True)),
                ('yil', models.DateField()),
                ('qimmatt_tr', models.CharField(blank=True, max_length=50, null=True)),
                ('qimmat_sotuv', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mavsum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_mavsum', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ims', models.CharField(max_length=50)),
                ('pozitsiya', models.CharField(max_length=50)),
                ('narx', models.CharField(max_length=50)),
                ('davlat', models.CharField(max_length=50)),
                ('t_yil', models.DateField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.club')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.CharField(max_length=50)),
                ('tah_narx', models.CharField(max_length=50)),
                ('eski', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eski_narx', to='football.club')),
                ('mavsum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.mavsum')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.player')),
                ('yangi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.club')),
            ],
        ),
    ]