from django import forms
from .models import *


class DataForm(forms.ModelForm):
    class Meta:
        model = DataSuratBebasLabkom
        fields = ['nama',
                  'nim',
                  'jenis_kelamin',
                  'program_studi',
                  'angkatan',
                  'hari',
                  'tanggal']
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
        }
        labels = {
            'nama': 'Nama ',
            'nim': 'NIM ',
            'jenis_kelamin': 'Jenis Kelamin ',
            'program_studi': 'Program Studi',
            'angkatan': 'Angkatan',
            'hari': 'Hari ',
            'tanggal': 'Tanggal ',
        }
        pass
    pass
