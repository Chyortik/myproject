from django.contrib import admin
from .models import Category, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """ Список продуктов """
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']  # сортировка строк
    list_filter = ['date_added', 'price']  # Добавление фильтрации в список изменения
    search_fields = ['description']  # Текстовый поиск
    search_help_text = 'Поиск по полю Описание продукта  (description)'  # Текстовый поиск
    actions = [reset_quantity]
    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added',
    #           'rating']  # не работает, когда включен fieldsets
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
