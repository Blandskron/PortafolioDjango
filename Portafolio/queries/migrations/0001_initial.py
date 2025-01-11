# Generated by Django 5.1.4 on 2025-01-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vendedor', models.CharField(max_length=100)),
            ],
        ),
    ]