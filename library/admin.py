from django.contrib import admin
from .models import Author, Book, Loan, Review


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Review)