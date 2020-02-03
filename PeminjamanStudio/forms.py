from django import forms


class DataForm(forms.Form):     # Form untuk PeminjamanStudioTambah.html
    nama = forms.CharField(
        label='Nama ',
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'Nama',
                'class': 'form-control',
                'placeholder': 'Masukkan nama',
            }
        )
    )

    nim = forms.CharField(
        label='NIM ',
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'NIM',
                'class': 'form-control',
                'placeholder': 'Masukkan NIM',
            }
        )
    )

    jenis_kelamin = forms.ChoiceField(
        label='Jenis Kelamin ',
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'NIM',
                'class': 'custom-select',
            },
        ),
        choices=[
            ('', ''),
            ("L", "Laki-laki"),
            ("P", "Perempuan"),
        ],
    )

    program_studi = forms.ChoiceField(
        label='Program Studi ',
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'ProgramStudi',
                'class': 'custom-select',
            }
        ),
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

    angkatan = forms.ChoiceField(
        label='Angkatan ',
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'Angkatan',
                'class': 'custom-select',
            }
        ),
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

    hari = forms.CharField(
        label='Hari ',
        max_length=7,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'Hari',
                'class': 'form-control',
                'placeholder': 'Masukkan hari'
            }
        )
    )

    tanggal = forms.CharField(
        label='Tanggal ',
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'Tanggal',
                'class': 'form-control',
                'placeholder': 'Masukkan Tanggal'
            }
        )
    )

    tempat = forms.CharField(
        label='Tempat ',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'Tempat',
                'class': 'form-control',
                'placeholder': 'Masukkan Tempat'
            }
        )
    )

    waktu = forms.CharField(
        label='Waktu ',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'Waktu',
                'class': 'form-control',
                'placeholder': 'Masukkan Waktu'
            }
        )
    )
    pass