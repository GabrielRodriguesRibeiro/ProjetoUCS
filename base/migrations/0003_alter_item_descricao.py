# Generated by Django 4.1.7 on 2023-06-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_item_cor_alter_item_descricao_tecnica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
