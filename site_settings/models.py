from django.db import models

class SiteSettings(models.Model):
    slider_per_page = models.PositiveIntegerField(default=3, help_text="Number of slides to show at once on desktop.")
    slider_per_move = models.PositiveIntegerField(default=1, help_text="Number of slides to move when a user clicks next/prev.")
    slider_gap = models.CharField(max_length=10, default="1rem", help_text="Gap between slides (e.g., '1rem', '20px').")

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteSettings, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Site Settings"