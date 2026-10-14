from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:loan_id>/', views.return_book, name='return_book'),
    path('history/', views.loan_history, name='loan_history'),
    path('register/', views.register, name='register'),
    path('review/<int:book_id>/', views.add_review,name='add_review' ),
    path('book/<int:book_id>/',views.book_detail,name='book_detail'),

]