# Generated by Django 2.0.8 on 2018-09-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTime', models.CharField(max_length=50)),
                ('estadio', models.CharField(max_length=50)),
                ('patrocinio', models.CharField(max_length=50)),
                ('nomeJogador', models.CharField(max_length=50)),
                ('nomeTecnico', models.CharField(max_length=50)),
            ],
        ),
    ]