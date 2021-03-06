# Generated by Django 3.0.7 on 2020-07-08 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=40)),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField(verbose_name='Data da Transação')),
                ('status', models.CharField(choices=[('nao_pago', 'Não Pago'), ('pago', 'Pago')], max_length=8)),
                ('tipo', models.CharField(choices=[('receita', 'Receita'), ('despesa', 'Despesa')], max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transacao',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('membros', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'grupo',
            },
        ),
    ]
