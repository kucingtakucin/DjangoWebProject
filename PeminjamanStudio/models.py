from django.db import models

# Create your models here.


class DataPeminjamanStudio(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=12)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=[
            ('', ''),
            ("L", "Laki-laki"),
            ("P", "Perempuan"),
        ]
    )
    program_studi = models.CharField(
        max_length=30,
        choices=[
            ('', ''),
            ("S1 Matematika", "S1 Matematika"),
            ("S1 Biologi", "S1 Biologi"),
            ("S1 Fisika", "S1 Fisika"),
            ("S1 Kimia", "S1 Kimia"),
            ("S1 Farmasi", "S1 Farmasi"),
            ("S1 Informatika", "S1 Informatika"),
            ("S1 Ilmu Lingkungan", "S1 Ilmu Lingkungan"),
            ("D3 Teknik Informatika", "D3 Teknik Informatika"),
            ("D3 Farmasi", "D3 Farmasi"),
        ]
    )
    angkatan = models.PositiveIntegerField(
        choices=[
            ('', ''),
            (2015, 2015),
            (2016, 2016),
            (2017, 2017),
            (2018, 2018),
            (2019, 2019),
            (2020, 2020),
        ]
    )
    hari = models.CharField(max_length=7)
    tanggal = models.CharField(max_length=25)
    tempat = models.CharField(max_length=100)
    waktu = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {} - {} - {} - {}".format(self.id, self.nama, self.nim, self.program_studi, self.angkatan)
        pass
    pass
    pass
