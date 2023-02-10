# Generated by Django 4.1.6 on 2023-02-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idVenta', models.TextField()),
                ('idProducto', models.TextField()),
                ('cantidad', models.TextField()),
                ('precio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
                ('imagen', models.TextField()),
                ('precio', models.TextField()),
                ('stock', models.TextField()),
                ('descuento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.TextField()),
                ('fecha', models.TextField()),
                ('total', models.TextField()),
            ],
        ),
    ]
