# Generated by Django 2.2 on 2019-05-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_id_func'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default='', upload_to='documento'),
            preserve_default=False,
        ),
    ]