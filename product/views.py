from django.core.paginator import Paginator
from django.views.generic import ListView
from django_filters.views import FilterView

from .util import show_results_filter_set
from .models import Product
from .filters import ProductFilter


class ProductView(FilterView):
    template_name = 'pesquisa.html'
    model = Product
    paginate_by = 10
    filterset_class = ProductFilter

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

        context['filter_url'] = ('&' + qr.urlencode() if len(qr) > 0 else '') 
        context['show_results'] =-show_results_filter_set(qr)
        context['filter'] = ProductFilter(
            data=self.request.GET, queryset=self.get_queryset()
        )
        return context