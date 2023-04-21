from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', admin.site.urls),
    path('',views.index,name='admin'),
    path('inventory/',views.inventory,name='inventory'),
    path('manage/',views.manage,name='manage'),
    path('update/',views.update,name='update'),
 

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
