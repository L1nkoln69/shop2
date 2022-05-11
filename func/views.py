from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, ListView, DetailView
from .forms import RegistrUserForm
from .models import Products
from basked.forms import CartAddProductForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('products')


def logout_user(request):
    logout(request)
    return redirect('products')


class RegistrationUser(FormView):
    form_class = RegistrUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super(RegistrationUser, self).form_valid(form)


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Products
    context_object_name = 'products'
    paginate_by = 20


class Search(ListView):
    template_name = 'product_list.html'
    model = Products
    context_object_name = 'products'

    def get_queryset(self):
        return Products.objects.filter(title__icontains=self.request.GET.get('search'))



class ProductDetail(DetailView):
    model = Products
    template_name = 'product.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'


def product_detail(request, id, slug):
    product = get_object_or_404(Products,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop2/func/template/product.html', {'product': product,
                                                        'cart_product_form': cart_product_form})