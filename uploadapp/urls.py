
from subscribe.views import thank_you
from . import views
from django.urls import path

urlpatterns = [
    path('image',views.upload_image,name='upload_image'),
    path('thank_you',views.thank_you,name='thank_you')
]
