# Generated by Django 5.1.4 on 2025-01-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=64)),
                ('product_len', models.SmallIntegerField()),
                ('thickness', models.SmallIntegerField()),
                ('width', models.SmallIntegerField()),
                ('material', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/kind')),
                ('kind', models.CharField(max_length=64)),
                ('product_len', models.SmallIntegerField()),
                ('thickness', models.SmallIntegerField()),
                ('width', models.SmallIntegerField()),
                ('material', models.CharField(max_length=32)),
            ],
        ),
    ]
