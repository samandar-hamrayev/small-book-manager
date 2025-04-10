from django.contrib import admin
from .models import Book


# Custom admin class for Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'isbn', 'publication_date')

    # Fields to filter by in the sidebar
    list_filter = ('author', 'publication_date')

    # Fields to search
    search_fields = ('title', 'author', 'isbn')

    # Fields to order by
    ordering = ('title',)

    # Fields to show in the detail view
    fields = ('title', 'author', 'isbn', 'publication_date')

# If you prefer not using the decorator, you can use this alternative:
# admin.site.register(Book, BookAdmin)