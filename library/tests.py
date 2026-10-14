from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Author, Book, Loan, Review


class LibraryTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='bea',
            password='test12345'
        )

        self.author = Author.objects.create(
            name='Autor de prueba'
        )

        self.book = Book.objects.create(
            title='Libro de prueba',
            author=self.author,
            available=True
        )

    def test_book_list_loads(self):
        response = self.client.get(
            reverse('book_list')
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_borrow_book(self):
        self.client.login(
            username='bea',
            password='test12345'
        )

        response = self.client.get(
            reverse(
                'borrow_book',
                args=[self.book.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Loan.objects.filter(
                user=self.user,
                book=self.book
            ).exists()
        )

        self.book.refresh_from_db()

        self.assertFalse(self.book.available)

    def test_user_can_return_book(self):
        self.client.login(
            username='bea',
            password='test12345'
        )

        loan = Loan.objects.create(
            user=self.user,
            book=self.book
        )

        self.book.available = False
        self.book.save()

        response = self.client.get(
            reverse(
                'return_book',
                args=[loan.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        loan.refresh_from_db()
        self.book.refresh_from_db()

        self.assertTrue(loan.returned)
        self.assertTrue(self.book.available)

    def test_loan_history_requires_login(self):
        response = self.client.get(
            reverse('loan_history')
        )

        self.assertEqual(response.status_code, 302)

    def test_user_can_create_review(self):
        self.client.login(
            username='bea',
            password='test12345'
        )

        response = self.client.post(
            reverse(
                'add_review',
                args=[self.book.id]
            ),
            {
                'rating': 5,
                'comment': 'Muy buen libro'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Review.objects.filter(
                user=self.user,
                book=self.book
            ).exists()
        )


