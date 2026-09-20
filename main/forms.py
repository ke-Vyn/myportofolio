from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from main.models import Project, Education


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/repo",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "description",
            "start_year",
            "end_year",
        ]

        labels = {
            "institution": "Institusi",
            "degree": "Gelar / Program Studi",
            "description": "Deskripsi",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "e.g. Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "e.g. S1 Sistem Informasi",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan fokus studi / pencapaian",
                    "rows": 3,
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "e.g. 2025",
                    "min": 1900,
                    "max": 2100,
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "e.g. 2029 (biarkan kosong jika masih berlangsung)",
                    "min": 1900,
                    "max": 2100,
                }
            ),
        }