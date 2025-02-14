from django.shortcuts import render,redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .models import Case,Catalog

from .models import Catalog, Case
from .forms import Catalog_Form

def blog(request):
    catalog_obj = Catalog.objects.all()
    return render(request, "shop/blog.html", context = {"catalog" : catalog_obj})

class Make_Catalog_Obj_View(PermissionRequiredMixin,FormView):
    permission_required = 'is_superuser'
    template_name = "shop/make_catalog_obj_view.html"
    form_class = Catalog_Form
    success_url = "/blog/"
    
    def permission_check(request):
        if not request.user.is_superuser: 
           return redirect("home")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
        
def Make_Case_View(request,catalog_obj):
    if request.method == "POST":
        
        catalog_ = Catalog.objects.get(pk=catalog_obj)
        user = request.user
        case_obj = Case()
        
        case_obj.client_id = user
        case_obj.client_phone = user.phone
        case_obj.client_adress = user.adress
        case_obj.catalog_id = catalog_
        case_obj.material = catalog_.material
        case_obj.kind = catalog_.kind
        case_obj.product_len = request.POST['product_len']
        case_obj.thickness = request.POST['thickness']
        case_obj.width = request.POST['width']
        case_obj.quantity = request.POST['quantity']

        case_obj.save()
        return redirect("blog")
        
    return render(request,"shop/make_case.html")

class Case_List_View(ListView):
    model = Case
    paginate_by = 100
    template_name = "case_list.html"
