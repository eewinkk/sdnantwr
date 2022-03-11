from django.db import models

# Table kegiatan realsi ke table aspek
class Kegiatan(models.Model):
    kegiatan = models.CharField(
        max_length=255, 
        db_index=True, 
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.kegiatan

# Table aspek 
class Aspek(models.Model):
    aspek = models.CharField(
        max_length=20, 
        db_index=True, 
        unique=True,
    )
    kegiatan = models.ManyToManyField(
        'Kegiatan', 
        blank=True, 
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.aspek

# Table lembar monitor
class LembarMonitoring(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )






