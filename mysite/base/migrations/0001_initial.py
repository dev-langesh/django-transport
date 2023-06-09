# Generated by Django 4.2 on 2023-04-22 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_no', models.IntegerField()),
                ('destination', models.CharField(max_length=200)),
                ('driver', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.bus')),
            ],
        ),
    ]
