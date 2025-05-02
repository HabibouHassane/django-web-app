from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons afficher dans la liste

class listingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'band') # liste les champs que nous voulons afficher dans la liste
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, listingsAdmin)



