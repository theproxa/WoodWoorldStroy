from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Catalog, Case
from .forms import Catalog_Form

def blog(request):
    catalog = Catalog.objects.all()
    return render(request, "shop/blog.html", context = {"catalog" : catalog})

class Make_Catalog_Obj_View(FormView):
    template_name = "shop/make_catalog_obj_view.html"
    form_class = Catalog_Form
    success_url = "/blog/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    



    