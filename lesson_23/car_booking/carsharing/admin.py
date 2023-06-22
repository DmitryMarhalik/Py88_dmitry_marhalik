from django.contrib import admin
from .models  import Brand,Auto,AutoModel

@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    pass


@admin.register(Auto)
class AdminAuto(admin.ModelAdmin):
    list_filter = ('auto_model','status')
    list_display = ('vin_code','status')


@admin.register(AutoModel)
class AdminAutoModel(admin.ModelAdmin):
    list_display = ('name', 'count')
    def count(self,instance):
        count= Auto.objects.filter(auto_model=instance).count()
        return count



