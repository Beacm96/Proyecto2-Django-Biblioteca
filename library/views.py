from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Book, Loan
from .forms import ReviewForm


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


def book_list(request):

    books = Book.objects.all()

    return render(request, 'library/book_list.html', {
        'books': books
    })


@login_required
def borrow_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if book.available:

        Loan.objects.create(
            user=request.user,
            book=book
        )

        book.available = False
        book.save()

    return redirect('book_list')


@login_required
def return_book(request, loan_id):

    loan = get_object_or_404(
        Loan,
        id=loan_id,
        user=request.user
    )

    if not loan.returned:

        loan.returned = True
        loan.return_date = timezone.now()
        loan.save()

        loan.book.available = True
        loan.book.save()

    return redirect('loan_history')


@login_required
def loan_history(request):

    loans = Loan.objects.filter(
        user=request.user
    ).order_by('-loan_date')

    return render(request, 'library/loan_history.html', {
        'loans': loans
    })


@login_required
def add_review(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user
            review.book = book

            review.save()

            return redirect('book_detail', book_id=book.id)

    else:

        form = ReviewForm()

    return render(request, 'library/add_review.html', {
        'form': form,
        'book': book
    })


def book_detail(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    reviews = book.review_set.all()

    return render(request, 'library/book_detail.html', {
        'book': book,
        'reviews': reviews
    })