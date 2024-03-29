# Generated by Django 4.1.7 on 2023-08-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PartyDetails',
        ),
    ]
