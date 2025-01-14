from django.urls import path 
from .views import blog,Make_Catalog_Obj_View

urlpatterns = [
    path('blog/', blog , name = "blog"),
    path('blog/make_catalog_obj_view/',Make_Catalog_Obj_View.as_view(),name = "make_catalog_obj_view"),
    
]