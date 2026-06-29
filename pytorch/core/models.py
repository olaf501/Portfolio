from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('GAME_DEV', 'Game Development'),
        ('VLSI', 'VLSI & Chip Design'),
        ('AI', 'Artificial Intelligence'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma-separated list (e.g., C++, Verilog, PyTorch)")
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"