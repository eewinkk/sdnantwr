from django.contrib import admin

# Register your models here.
from .models import (
 Kegiatan,
 Aspek
)

#-------------------------------------------
# Kumpulan register model dari Master Data
#-------------------------------------------
admin.site.register(Kegiatan)
admin.site.register(Aspek)

