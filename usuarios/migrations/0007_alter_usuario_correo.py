# Generated by Django 3.2.16 on 2023-02-12 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='sin_correo@gmail.com', max_length=100),
        ),
    ]
