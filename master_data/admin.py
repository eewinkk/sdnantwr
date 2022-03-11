from django.contrib import admin

# Register your models here.
from .models import (
    Kelas,
	Guru,
    Santri
)

class GuruAdmin(admin.ModelAdmin):
    list_display = [
		'nama_Lengkap', 
		'kelas_Diampu', 
		'nomer_Telpon',
        'kota', 
		'alamat_Lengkap', 
	]
    list_filter = (
		'kota', 
	)
    search_fields = [
        'nama_Lengkap', 
	]
    readonly_fields = (
		'alamat_Lengkap',
	)

class SantriAdmin(admin.ModelAdmin):
    list_display = [
        'nisn',
		'nama_Lengkap', 
		'ttl', 
		'kelas',
        'telp_Wali',
        'kota', 
		'alamat_Lengkap', 
	]
    list_filter = (
        'kelas__kelas',
		'kota', 
	)
    search_fields = [
	    'nisn',
        'nama_Lengkap', 
	]
    readonly_fields = (
		'alamat_Lengkap',
	)


#-------------------------------------------
# Kumpulan register model dari Master Data
#-------------------------------------------
admin.site.register(Kelas)
admin.site.register(Guru, GuruAdmin)
admin.site.register(Santri, SantriAdmin)