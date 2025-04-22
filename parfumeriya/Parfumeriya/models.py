import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Kategoriya(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=255)
    rasm = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ism)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ism


class Eslatma(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=255)
    tarkibi = models.TextField()
    rasm = models.URLField()

    def __str__(self):
        return self.ism


class Mahsulot(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=255)
    mini_tavsif = models.CharField(max_length=255)
    tavsif = models.TextField()
    narx = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    kalit_slova = models.JSONField(default=list)  # ["yangi", "erkaklar", "bahor"]
    eslatmalar = models.ManyToManyField(Eslatma, related_name='mahsulotlar', blank=True)
    ball = models.FloatField(default=0)
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE, related_name='mahsulotlar')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.ism.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ism


class Variant(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='variantlar')
    hajm = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mahsulot.ism} - {self.hajm}"


class Sharh(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='sharhlar')
    ball = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    sharh = models.TextField()
    moderatsiya_qilingan = models.BooleanField(default=False)
    moderator = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.mahsulot.ism} uchun sharh - {self.ball}⭐"


class Blog(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=255)
    mini_tavsif = models.CharField(max_length=255)
    tavsif = models.TextField()
    kalit_slova = models.JSONField(default=list)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.ism.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ism


class Banner(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=255)
    rasm = models.URLField()
    havola_na_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='bannerlar')

    def __str__(self):
        return f"Banner: {self.ism}"
