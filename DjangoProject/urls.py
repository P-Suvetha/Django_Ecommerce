from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('Inventory.urls')),
    path('orders/',include('OrderManagement.urls')),
    path('', include('authentication.urls')),
    path('.well-known/appspecific/com.chrome.devtools.json', lambda request: JsonResponse({})),

]
