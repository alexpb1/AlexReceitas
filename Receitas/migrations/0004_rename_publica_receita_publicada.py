# Generated by Django 3.2.5 on 2021-07-25 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas', '0003_receita_publica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='publica',
            new_name='publicada',
        ),
    ]