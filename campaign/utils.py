from django.utils.text import slugify


def get_unique_slug(model_instance, sluggable_field_name, slug_field_name):
    slug = slugify(getattr(model_instance, sluggable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass.objects.filter(
        **{slug_field_name: unique_slug}
        ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1

    return unique_slug
