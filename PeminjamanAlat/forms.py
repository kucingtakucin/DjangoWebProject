from django import forms
from .models import *


class DataForm(forms.ModelForm):
    class Meta:
        model = DataPeminjamanAlat
        fields = ['nama',
                  'nim',
                  'jenis_kelamin',
                  'program_studi',
                  'angkatan',
                  'hari',
                  'tanggal',
                  'tempat',
                  'waktu',
                  'alat',
                  'jumlah',
                  'lama_peminjaman',
                  'harga',
                  'keperluan']
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'id': 'Nama',
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama',
                }
            ),
            'nim': forms.TextInput(
                attrs={
                    'id': 'NIM',
                    'class': 'form-control',
                    'placeholder': 'Masukkan NIM',
                }
            ),
            'jenis_kelamin': forms.Select(
                attrs={
                    'id': 'NIM',
                    'class': 'custom-select',
                }
            ),
            'program_studi': forms.Select(
                attrs={
                    'id': 'ProgramStudi',
                    'class': 'custom-select',
                }
            ),
            'angkatan': forms.Select(
                attrs={
                    'id': 'Angkatan',
                    'class': 'custom-select',
                }
            ),
            'hari': forms.TextInput(
                attrs={
                    'id': 'Hari',
                    'class': 'form-control',
                    'placeholder': 'Masukkan hari'
                }
            ),
            'tanggal': forms.TextInput(
                attrs={
                    'id': 'Tanggal',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Tanggal'
                }
            ),
            'tempat': forms.TextInput(
                attrs={
                    'id': 'Tempat',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Tempat'
                }
            ),
            'waktu': forms.TextInput(
                attrs={
                    'id': 'Waktu',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Waktu'
                }
            ),
            'alat': forms.Select(
                attrs={
                    'id': 'Alat',
                    'class': 'custom-select'
                }
            ),
            'jumlah': forms.NumberInput(
                attrs={
                    'id': 'Jumlah',
                    'class': 'form-control',
                }
            ),
            'lama_peminjaman': forms.Select(
                attrs={
                    'id': 'LamaPeminjaman',
                    'class': 'custom-select',
                }
            ),
            'harga': forms.NumberInput(
                attrs={
                    'id': 'Harga',
                    'class': 'custom-select',
                }
            ),
            'keperluan': forms.Textarea(
                attrs={
                    'id': 'Keperluan',
                    'class': 'form-control',
                    'rows': '4',
                    'placeholder': 'Masukkan keperluan'
                }
            )
        }
        labels = {
            'nama': 'Nama ',
            'nim': 'NIM ',
            'jenis_kelamin': 'Jenis Kelamin ',
            'program_studi': 'Program Studi ',
            'angkatan': 'Angkatan ',
            'hari': 'Hari ',
            'tanggal': 'Tanggal ',
            'tempat': 'Tempat ',
            'waktu': 'Waktu ',
            'alat': 'Alat ',
            'jumlah': 'Jumlah ',
            'lama_peminjaman': 'Lama Peminjaman ',
            'harga': 'Harga ',
            'keperluan': 'Keperluan ',
        }
