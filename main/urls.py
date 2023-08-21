from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),
    path('<int:pk>/deletecom', views.DeleteCom.as_view(), name='deletecom'),
    path('validate', views.validate, name='validate'),
    path('reg', views.reg, name='reg'),
    path('logout', views.userlogout, name='logout'),
]
