import uuid
from django.db.models import TextChoices


class SaveMediaFiles(object):

    def product_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/product/{uuid.uuid4()}.{image_extension}'

    def clientcomment_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/clientcomment/{uuid.uuid4()}.{image_extension}'

    def blog_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/blog/{uuid.uuid4()}.{image_extension}"