# Generated by Django 4.0.4 on 2022-11-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaAgendada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('medico', models.CharField(max_length=100)),
                ('especialidade_medico', models.CharField(max_length=60)),
                ('paciente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=100)),
                ('cpf_funcionario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField()),
                ('hospital', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=100)),
                ('cpf_paciente', models.CharField(max_length=20, unique=True)),
                ('convenio', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('dataDeEntrada', models.DateField(blank=True, null=True)),
                ('dataDeSaida', models.DateField(blank=True, null=True)),
            ],
        ),
    ]