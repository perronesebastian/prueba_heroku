# Generated by Django 4.0 on 2021-12-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='fecha_modificacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificacion'),
        ),
    ]
