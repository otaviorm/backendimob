# Generated by Django 4.2.7 on 2023-11-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_anuncio'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='descricao',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='endereco',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tamanho',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='vagas',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
