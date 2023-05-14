from django.conf import settings

def my_image(request):
    image_url = None
    if request.user.is_authenticated:
        image_url = request.user.image.url
    return {'MY_IMAGE_URL': image_url}
