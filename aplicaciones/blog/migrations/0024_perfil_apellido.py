# Generated by Django 4.0 on 2022-01-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_perfil_escritor'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='apellido',
            field=models.CharField(max_length=200, null=True),
        ),
    ]