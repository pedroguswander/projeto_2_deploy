# Generated by Django 5.1.1 on 2024-10-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_material_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brinquedo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brinquedo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('passo_a_passo', models.TextField()),
            ],
        ),
    ]
