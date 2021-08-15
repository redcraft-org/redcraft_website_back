from django.db import models


class File(models.Model):
    FILE_PROCESSORS = (
        ('s3', 's3'),
        ('f', 'folder'),
    )

    ref = models.CharField(max_length=64)
    meta = models.JSONField(max_length=64)
    file_processor = models.CharField(max_length=2, choices=FILE_PROCESSORS)

    def __str__(self):
        return f"<File: {self.ref}>"
