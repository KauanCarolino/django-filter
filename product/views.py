from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Product

class ProductView(ListView):
    template_name = 'pesquisa.html'
    model = Product
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qr = self.request.GET.copy()

        page = self.request.GET.get('page')
        
        product_list = self.get_queryset()
        paginator = Paginator(product_list, self.paginate_by)
        page_obj = paginator.get_page(page)
        
        context['page_obj'] = page_obj
        return context