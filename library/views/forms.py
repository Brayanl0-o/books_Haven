"""
Control y validación de formularios.
"""
from django import forms
from ..models.book import Book
from ..models.author import Author
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

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'death_date', 'biography', 'photo_author']


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = [
#             'name',
#             'birth_date',
#             'death_date',
#             'biography',
#             'photo_author',
#             'books'
#         ]
#     def save(self, commit =True):
#         instance = super().save(commit=False)


#         if commit:
#             instance.save()

#         instance.books.set(self.cleaned_data['books'])

#         if commit:
#             instance.save()
#         return instance 
  