# Generated by Django 5.0.2 on 2024-03-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=72)),
                ('company', models.CharField(max_length=36)),
                ('color', models.CharField(max_length=16)),
                ('RAM', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('price', models.FloatField()),
                ('img_url', models.CharField(max_length=124)),
            ],
        ),
    ]
