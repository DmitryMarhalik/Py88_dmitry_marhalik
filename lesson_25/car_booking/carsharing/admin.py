from django.contrib import admin
from .models import Brand, Auto, AutoModel, User, Image
from django.utils.safestring import mark_safe


class AutoModelInline(admin.TabularInline):
    model = AutoModel


def set_status_free(admin_model, request, queryset):
    queryset.update(status='free')


def set_status_booked(admin_model, request, queryset):
    queryset.update(status='booked')


def set_status_taken(admin_model, request, queryset):
    queryset.update(status='taken')


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'phone', 'auto')
    # list_filter = ('auto_model','user','status')
    search_fields = ('phone',)
    # ordering = ('name',)
    list_filter = ('name', 'phone')

    def auto(self, instance):
        a = Auto.objects.filter(user=instance)
        if a:
            return a[0]
        return '-'


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ('name', 'preview_pict', 'count')
    ordering = ('name',)
    inlines = [AutoModelInline]
    readonly_fields = ('preview_pict',)

    def count(self, instance):
        count = AutoModel.objects.filter(brand=instance).count()
        return count

    def preview_pict(self, instance: Brand):

        if not instance.image:
            return mark_safe(f'<b>without logo</b>')
        else:
            return mark_safe(f'<img src="/media/{instance.image.url_image}" style ="max-width:40px">')


@admin.register(Auto)
class AdminAuto(admin.ModelAdmin):
    list_filter = ('auto_model', 'user', 'status')
    list_display = ('auto_model', 'vin_code', 'status', 'user')
    search_fields = ('vin_code',)
    list_display_links = ('user', 'auto_model')
    actions = [set_status_free, set_status_booked, set_status_taken]


@admin.register(AutoModel)
class AdminAutoModel(admin.ModelAdmin):
    list_display = ('name', 'count')
    list_filter = ('brand',)
    ordering = ('name',)

    def count(self, instance):
        count = Auto.objects.filter(auto_model=instance).count()
        return count


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('title', 'url_image')
