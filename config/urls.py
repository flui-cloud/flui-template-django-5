from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from items import views as item_views

urlpatterns = [
    path('', item_views.home, name='home'),
    path('health/', item_views.health, name='health'),
    path('items/', item_views.ItemListCreateView.as_view(), name='item-list'),
    path('items/<str:pk>/', item_views.ItemDetailView.as_view(), name='item-detail'),
    path('api/openapi/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
