from django.db import models
import datetime

#-------------------------------------------
# Pihak ke3 
#-------------------------------------------
from phonenumber_field.modelfields import PhoneNumberField

# Tabel kelas relasi ke tabel Santri dan Guru
class Kelas(models.Model):
    kelas_Id = models.BigAutoField(
        primary_key=True,
        db_index=True,
    )
    kelas = models.CharField(
        max_length=5,
        unique=True,
        db_index=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name_plural = 'Data Kelas'

    def __str__(self):
        return self.kelas

# Tabel ali Kelas relasi ke tabel SantriW
class Guru(models.Model):
    TITLE_GURU = [
            ('u', 'Ust.'),
            ('h', 'Usth.'),
        ]

    title_Guru = models.CharField(
        max_length=1,
        choices=TITLE_GURU, 
        blank=True,
    ) 
    nama_Lengkap = models.CharField(
        max_length=50, 
        db_index=True
    )
    ttl =  models.DateField(
        blank=True,
        verbose_name='TTL',
    )
    kelas_Diampu = models.ForeignKey(
        Kelas, 
        default=None, 
        on_delete=models.CASCADE,
    )
    alamat = models.CharField(
        max_length=100,
        help_text="Nama jalan, blok, desa, RT/RW atau kelurahan", 
    )
    kota = models.CharField(
        max_length=20
    )
    provinsi = models.CharField(
        max_length=20
    )
    kode_pos = models.CharField(
        max_length=10,
        blank=True
    )
    nomer_Telpon = PhoneNumberField(
        help_text="Nomer telpon <em>(e.g. +621334064094)</em>.", 
        blank=True
    )
    foto = models.ImageField(
        upload_to='fotosantri/', 
        null=True, 
        blank=True,
    )
    alamat_Lengkap = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name_plural = 'Data Guru'

    def __str__(self):
        return '{0} {1}'.format(
            self.title_Guru,
            self.nama_Lengkap,
        )

    # Gabungan dari field detail alamat
    def get_alamat_lengkap(self):
        return '{0} {1} {2} {3}'.format(
            self.alamat, 
            self.kota, 
            self.provinsi, 
            self.kode_pos
            )
    
    # Simpan alamat_lengkap ke database
    def save(self, *args, **kwargs):
        self.alamat_Lengkap = str(self.get_alamat_lengkap())
        super().save(*args, **kwargs)

# Tabel santri
class Santri(models.Model):
    STATUS_SANTRI = [
        ('l', 'Putra'),
        ('p', 'Putri'),
    ]

    GOLONGAN_DARAH = [
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'AB'),
        ('4', 'O'),
    ]

    nisn = models.CharField(
        max_length=100, 
        unique=True, 
        db_index=True,
        verbose_name='NISN',
        blank=True,
        null=True,
    )
    nama_Lengkap = models.CharField(
        max_length=50, 
        db_index=True
    )
    ttl =  models.DateField(
        blank=True,
        verbose_name='TTL',
    )
    kelas = models.ForeignKey(
        Kelas, 
        default=None, 
        on_delete=models.CASCADE,
    )
    status_Santri = models.CharField(
        max_length=1,
        choices=STATUS_SANTRI, 
        blank=True,
    ) 
    alamat = models.CharField(
        max_length=100,
        help_text="Nama jalan, blok, desa, RT/RW atau kelurahan", 
    )
    kota = models.CharField(
        max_length=20
    )
    provinsi = models.CharField(
        max_length=20
    )
    kode_pos = models.CharField(
        max_length=10,
        blank=True
    )
    telp_Wali = PhoneNumberField(
        help_text="Isi dengan nomer telfon orang tua wali <em>(e.g. +621334064094)</em>.", 
        blank=True
    )
    tinggi_Badan = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Tinggi badan (CM)',
    )
    berat_Badan = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Berat badan (KG)',
    )
    golongan_Darah = models.CharField(
        max_length=1,
        choices=GOLONGAN_DARAH, 
        blank=True,
    ) 
    riwayat_Penyakit = models.CharField(
        max_length=100,
        blank=True,
    )
    nama_ortu = models.CharField(
        max_length=50, 
        blank=True,
        verbose_name='Nama Orang Tua',
    )
    foto = models.ImageField(
        upload_to='fotosantri/', 
        null=True, 
        blank=True,
    )
    alamat_Lengkap = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nama_Lengkap

    class Meta:
        verbose_name_plural = 'Data Santri'

    # Gabungan dari field detail alamat
    def get_alamat_lengkap(self):
        return '{0} {1} {2} {3}'.format(
            self.alamat, 
            self.kota, 
            self.provinsi, 
            self.kode_pos
            )
    
    # Simpan alamat_lengkap ke database
    def save(self, *args, **kwargs):
        self.alamat_Lengkap = str(self.get_alamat_lengkap())
        super().save(*args, **kwargs)

