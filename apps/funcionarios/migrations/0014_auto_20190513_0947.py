# Generated by Django 2.2 on 2019-05-13 12:47

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0013_auto_20190507_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14),
        ),
    ]
