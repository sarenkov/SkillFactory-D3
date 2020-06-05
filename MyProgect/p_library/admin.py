from django.contrib import admin
from p_library.models import Book, Author, Publisher





@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ['year_release', 'copy_count']
    list_display = ['title', 'author', 'publisher']
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')
    exclude = ['price']

@admin.register(Publisher)
class BookAdmin(admin.ModelAdmin):
    list_filter = ['name', 'city']
    list_display = ['name', 'city']    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['birth_year', 'country']
    list_display = ['full_name', 'country', 'birth_year', 'publisher']
    actions = ['ru_for_all']

    def ru_for_all(self, request, queryset):
        rows_updated = queryset.update(country='RU')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    ru_for_all.short_description = 'Сделать всех русскими'

