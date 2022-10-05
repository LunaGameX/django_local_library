from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    pass


admin.site.register(Author, AuthorAdmin)  # либо @register


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    inlines = [BooksInstanceInline]
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    pass


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    pass


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    pass

class MyView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'





