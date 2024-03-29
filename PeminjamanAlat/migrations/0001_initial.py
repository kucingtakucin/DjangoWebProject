# Generated by Django 3.0.2 on 2020-02-02 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPeminjamanAlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(max_length=10)),
                ('program_studi', models.CharField(max_length=20)),
                ('angkatan', models.IntegerField()),
                ('hari', models.CharField(max_length=10)),
                ('tanggal', models.CharField(max_length=20)),
                ('tempat', models.CharField(max_length=60)),
                ('waktu', models.CharField(max_length=40)),
                ('alat', models.CharField(max_length=100)),
                ('jumlah', models.IntegerField()),
                ('lama_peminjaman', models.CharField(max_length=10)),
                ('harga', models.IntegerField()),
                ('keperluan', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
