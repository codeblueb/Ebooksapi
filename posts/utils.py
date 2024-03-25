import string, random
from django.utils.text import slugify

def random_string_generator(size=17, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size) )

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance)