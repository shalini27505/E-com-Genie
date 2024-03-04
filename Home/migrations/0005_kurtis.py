# Generated by Django 5.0.2 on 2024-03-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_chanel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurtis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]
