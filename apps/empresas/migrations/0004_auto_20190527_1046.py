# Generated by Django 2.2 on 2019-05-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20190423_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(help_text='CNPJ da empresa', max_length=14, unique=True),
        ),
    ]
