from django.urls import path 
from .views import blog, Make_Catalog_Obj_View, Make_Case_View,Case_List_View

urlpatterns = [
    path('blog/', blog , name = "blog"),
    path('blog/make_catalog_obj_view/',Make_Catalog_Obj_View.as_view(),name = "make_catalog_obj_view"),
    path("blog/make_case/<int:catalog_obj>", Make_Case_View, name="make_case"),
    path("blog/case_list/",Case_List_View.as_view(),name="case_list")
]