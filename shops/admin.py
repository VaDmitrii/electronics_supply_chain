from django.contrib import admin, messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

from shops.models import Products, FactoryStore, Retailer, Entrepreneur


@admin.action(description="Очистить задолженность")
def clean_credit(modeladmin, request, queryset):
    updated = queryset.update(credit=0)
    modeladmin.message_user(
        request,
        ngettext(
            "%d задолженность была обнулена.",
            "%d задолженности были обнулены.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ("title", "supplier_link",)
    readonly_fields = ("supplier_link",)
    ordering = ("title",)
    actions = (clean_credit,)
    list_filter = ("city",)

    def supplier_link(self, entrepreneur):
        if entrepreneur.supplier in FactoryStore.objects.all():
            url = reverse("admin:shops_factorystore_change", args=[entrepreneur.supplier.id])
        else:
            url = reverse("admin:shops_retailer_change", args=[entrepreneur.supplier.id])
        link = '<a href="%s">%s</a>' % (url, entrepreneur.supplier.title)
        return mark_safe(link)

    supplier_link.short_description = 'Поставщик'


class RetailerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "supplier_link",
    )
    readonly_fields = ("supplier_link",)
    ordering = ("title",)
    actions = (clean_credit,)
    list_filter = ("city",)

    def supplier_link(self, retailer):
        url = reverse("admin:shops_factorystore_change", args=[retailer.supplier.id])
        link = '<a href="%s">%s</a>' % (url, retailer.supplier.title)
        return mark_safe(link)

    supplier_link.short_description = 'Поставщик'


class FactoryStoreAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_filter = ("city",)


admin.site.register(Products)
admin.site.register(FactoryStore, FactoryStoreAdmin)
admin.site.register(Retailer, RetailerAdmin)
admin.site.register(Entrepreneur, EntrepreneurAdmin)
