from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views.base_views import SearchView
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    queryset = Product.objects.filter(amount__gt=0)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
