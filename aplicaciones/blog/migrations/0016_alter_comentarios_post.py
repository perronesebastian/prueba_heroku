# Generated by Django 4.0 on 2021-12-21 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comentarios_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.post'),
        ),
    ]
