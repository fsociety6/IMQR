from django.utils import timezone

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .models import Item, Service, Category
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required, permission_required


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(form.cleaned_data)
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard');
        loginform = LoginForm()
    return render(request, "registration/login.html", {"loginform": loginform})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'inventory/registration/register.html', {"form": form})


# class ItemCreateView(LoginRequiredMixin, CreateView):
#     model = Item
#     fields = ['name', 'serial_number', 'category', 'details']
#     success_url = '/items/create_item'
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)

def ItemCreateView(request):
    if request.method == "GET":
        product_category = Category.objects.all()
        serial_number = request.GET.get(
            'serial_number')  # Replace the serial_number parameter with the keyword specified in the POST request.
        if serial_number == None:
            redirect('dashboard/')
        return render(request, 'imqr/item_create_form.html',
                      {'serial_number': serial_number, 'product_category': product_category})

    if request.method == "POST":
        category_object_id = request.POST.get('category')
        item = Item.objects.create(serial_number=request.POST.get('serial_number'), details=request.POST.get('details'),
                                   name=request.POST.get('product_name'),
                                   category=Category.objects.get(category_id=category_object_id),
                                   date_of_installation=timezone.now())
        servcie = Service.objects.create(item_id=item, details='Item Created', date_of_service=timezone.now(),
                                         updated_by=request.user)
        return redirect('/item/' + str(item.id))


def ItemDetailView(request, pk):
    item = get_object_or_404(Item, id=pk)
    service = Service.objects.filter(item_id=pk)
    last_updated_service = service.order_by('-date_of_service')
    f = last_updated_service.first()
    return render(request, 'imqr/item_detail.html',
                  {'item': item, 'service': service, 'last_updated_service': f})


# for creating the service.
def CreateServiceView(request, item_id):
    if request.method == "GET":
        product_object = get_object_or_404(Item, category_id=item_id)
        return render(request, 'imqr/service_create_form.html',
                      {'product_object': product_object})
    return HttpResponse('404 Error')


# class ItemDeleteView(LoginRequiredMixin, DeleteView):
#     model = Item
#     success_url = reverse_lazy("login")
#
#     def test_func(self):
#         post = self.get_object()  # This will return the post which we are going to update
#         if post.author == self.request.user:
#             return True
#         return False


@login_required(login_url='/login')
def dashboard(request):
    # For Getting Service History of the Current Logged In User.
    Service_History = Service.objects.filter(updated_by=request.user)
    return render(request, 'imqr/index.html', {'Service_History': Service_History})


def scancode(request):
    if request.method == "GET":
        return render(request, 'imqr/scan.html')

@login_required(login_url='/login')
def mainview(request):
    return redirect('/dashboard')

def CategoryCreateView(request):
    if request.method == "POST":
        Category.objects.create(category_name=request.POST.get('category_name'), category_created_by=request.user)
    return render(request, 'imqr/category_create.html')

