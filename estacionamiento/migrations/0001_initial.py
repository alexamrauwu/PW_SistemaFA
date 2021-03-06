# Generated by Django 3.2.2 on 2021-06-03 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('Id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sistema',
            fields=[
                ('Id_color', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ap_pat', models.CharField(max_length=30)),
                ('ap_mat', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('Id_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.sistema')),
            ],
        ),
        migrations.CreateModel(
            name='autos',
            fields=[
                ('Id_auto', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('horaE', models.TimeField()),
                ('horaS', models.TimeField()),
                ('descripcion', models.CharField(max_length=60)),
                ('Id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.administrador')),
                ('Id_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.sistema')),
            ],
        ),
    ]
