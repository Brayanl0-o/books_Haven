"""
Control y validación de formularios.
"""
from django import forms
from ..models.book import Book

class BookForm(forms.ModelForm):
    """
    Formulario y validación.
    """
    class Meta:
        """
        Formulario personalizado.
        """
        model = Book
        fields = [
            'name',
            'author',
            'cover_page' ,
            'link_dowload_free',
            'link_dowload_buy',
            'genre',
            'release_date',
            'number_pages',
            'summary'
        ]
    def clean_number_pages(self):
        """
        Validacion campo paginas.
        """
        number_pages = self.cleaned_data['number_pages']
        if number_pages is not None and number_pages < 1:
            raise forms.ValidationError("El número de páginas debe ser igual o mayor que 1.")
        return number_pages