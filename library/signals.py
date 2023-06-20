# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models.author import Author
# from .models.book import Book

# @receiver(pre_save, sender=Book)
# def update_author_on_book_save(sender, instance, **kwargs):
#     if instance.author is not None:
#         author = instance.author
#         current_books = author.books.all()
#         if instance not in current_books:
#             author.books.add(instance)
#             current_books.exclude(pk=instance.pk).delete()
#         else:
#             current_author = instance.author
#             if current_author != author:
#                 instance.author = author
#                 instance.save()
#                 current_books.exclude(pk=instance.pk).delete()


# from django.db.models.signals import m2m_changed, pre_save
# from django.dispatch import receiver
# from .models.author import Author
# from .models.book import Book


# @receiver(m2m_changed, sender=Author.books.through)
# def update_author_on_book_change(sender, instance, action, reverse, model, pk_set, **kwargs):
#     if action == 'pre_clear' and not reverse:
       
#         model.objects.filter(pk__in=pk_set).update(author=None)


# @receiver(pre_save, sender=Book)
# def update_author_on_book_save(sender, instance, **kwargs):
#     if instance.author_id is not None:
#         author = Author.objects.get(pk=instance.author_id)
#         current_books = author.books.all()
#         if instance not in current_books:
#             author.books.add(instance)
#             current_books.exclude(pk=instance.pk).delete()
#         else:
#             current_author = instance.author
#             if current_author != author:
#                 current_books.exclude(pk=instance.pk).update(author=None)
#                 instance.author = author
#                 instance.save()