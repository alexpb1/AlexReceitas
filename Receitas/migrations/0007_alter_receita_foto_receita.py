# Generated by Django 3.2.5 on 2021-07-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas', '0006_alter_receita_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]