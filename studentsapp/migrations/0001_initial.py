# Generated by Django 2.0 on 2020-06-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cSex', models.CharField(default='M', max_length=2)),
                ('cBirthday', models.DateField()),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('cPhone', models.CharField(blank=True, default='', max_length=50)),
                ('cAddr', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
