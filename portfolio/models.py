from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Se actualiza solo  en creación de instancia
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización") # Se ejecuta cada vez que se actualiza una instancia
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering= ["-created"]
    def __str__(self): 
        return self.title