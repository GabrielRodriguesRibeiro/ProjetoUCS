# Generated by Django 4.1.7 on 2023-06-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_item_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='staticfiles/imagens/'),
        ),
    ]
