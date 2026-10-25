from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ProductForm
from .models import Product


def menu_list(request):
    qs = Product.objects.filter(is_available=True)
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    page = Paginator(qs, 9).get_page(request.GET.get('page'))
    return render(request, 'menu/list.html', {'page': page, 'q': q})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'menu/detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ເພີ່ມສິນຄ້າສຳເລັດແລ້ວ')
            return redirect('menu_list')
    else:
        form = ProductForm()
    return render(request, 'menu/form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,
                           instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'ແກ້ໄຂແລ້ວ')
            return redirect('product_detail',
                            pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'menu/form.html',
        {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'ລຶບແລ້ວ')
        return redirect('menu_list')
    return render(request,
        'menu/confirm_delete.html',
        {'product': product})
