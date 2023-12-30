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
    # def save(self, commit=True):
    #     # Desvincula el libro del autor anterior antes de guardar
    #     old_author = self.instance.author
    #     if old_author:
    #         old_author.books.remove(self.instance)
    #         print(f"Libro desvinculado del autor anterior: {self.instance} del autor: {old_author.name}")
    #     # Guarda el formulario y el libro
    #     book = super().save(commit=commit)

    #     # Asocia el libro con el nuevo autor
    #     new_author = self.cleaned_data['author']
    #     new_author.books.add(book)
    #     print(f"Libro asociado al nuevo autor: {self.instance} al autor: {new_author}")
        
    #     return book
    # def clean_number_pages(self):
    #     """
    #     Validacion campo paginas.
    #     """
    #     number_pages = self.cleaned_data['number_pages']
    #     if number_pages is not None and number_pages < 1:
    #         raise forms.ValidationError("El número de páginas debe ser igual o mayor que 1.")
    #     return number_pages

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
  