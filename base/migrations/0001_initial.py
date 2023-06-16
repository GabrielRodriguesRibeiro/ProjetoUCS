# Generated by Django 4.1.7 on 2023-06-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tamanho', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('estoque', models.IntegerField()),
                ('descricao', models.TextField()),
                ('descricao_tecnica', models.TextField()),
            ],
        ),
    ]