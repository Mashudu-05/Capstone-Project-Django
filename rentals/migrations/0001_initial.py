# Generated by Django 5.1.7 on 2025-05-02 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='dresses/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
