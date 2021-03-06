from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


# Define the admin class
class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('id', 'book', 'due_back', 'status')
    fieldsets = (
        ('', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availabilty', {
            'fields': ('status', 'due_back')
        })
    )

