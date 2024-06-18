from django.contrib import admin
from .models import Product, ClientComment, TeamSays, Blog, Users
from import_export.admin import ImportExportModelAdmin


admin.site.register(Users)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    search_fields = ('name', 'price')
    ordering = ('id',)




@admin.register(ClientComment)
class ClientCommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'comment', 'product')
    list_display_links = ('id', 'name', 'comment', 'product')
    search_fields = ('name', 'comment', 'product')
    ordering = ('id',)


@admin.register(TeamSays)
class TeamSaysAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    search_fields = ('name', )
    ordering = ('id', )