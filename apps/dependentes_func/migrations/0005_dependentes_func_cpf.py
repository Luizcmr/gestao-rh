# Generated by Django 2.2 on 2019-07-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependentes_func', '0004_remove_dependentes_func_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependentes_func',
            name='cpf',
            field=models.CharField(blank=True, help_text='CPF do dependente', max_length=14, null=True),
        ),
    ]
