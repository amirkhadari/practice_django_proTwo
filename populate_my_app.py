import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django
django.setup()

import random
from my_app.models import Author, Genre, Book
from faker import Faker

fakegen = Faker()

genre = ['Social', 'History', 'Fictional', 'Comic', 'Romantic', 'Philosophy']

def add_genre():
    t = Genre.objects.get_or_create(name=random.choice(genre))[0]
    t.save()
    return t

def add_author():
    f_name = fakegen.first_name()
    l_name = fakegen.last_name()

    birth = fakegen.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=87)
    death = fakegen.date()

    writer = Author.objects.get_or_create(first_name=f_name, last_name=l_name,
    date_of_birth=birth, date_of_death=death)[0]
    writer.save()

    return writer


def add_book(N=5):
    for entry in range(N):
        book_name = fakegen.name_nonbinary()
        writ = add_author()
        desc = fakegen.paragraph(nb_sentences=5)
        gen = add_genre()
        isbn_no = fakegen.isbn13(separator='-')

        # new_book = Book.objects.get_or_create(title=book_name, isbn=isbn_no, author = writ,
        #  summary=desc, new_book.genre.add(gen))

        new_book = Book.objects.filter(title=book_name, isbn=isbn_no, author = writ,
         summary=desc, genre=gen)

        new_book = Book.objects.create(title=book_name, isbn=isbn_no, author = writ, summary=desc)
        new_book.genre.add(gen)


if __name__ == "__main__":
    print('populating script')
    add_book(N=20)
    print('populating script completed')
