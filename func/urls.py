from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('search', Search.as_view(), name='search'),
    path('product/<pk>', ProductDetail.as_view(), name='product'),

    path('registration/', RegistrationUser.as_view(), name='registr'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)