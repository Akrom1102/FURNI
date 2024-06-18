from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, ClientComment, Blog, TeamSays
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopPageView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        is_admin = request.user.is_staff  # or request.user.is_superuser
        if not search:
            context = {
                'products': products,
                'client_comments': client_comments,
                'search': search,
                'is_admin': is_admin
            }
            return render(request, 'shop.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {
                    'products': products,
                    'client_comments': client_comments,
                    'search': search
                }
                return render(request, 'shop.html', context)
            else:
                context = {
                    'products': products,
                    'client_comments': client_comments,
                    'search': search
                }
                return render(request, 'shop.html', context)


class ContactPageView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        context = {
            'products': products,
            'client_comments': client_comments,
        }
        return render(request, 'contact.html', context)


class ProductDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        client_comments = ClientComment.objects.all()
        return render(request, 'shop-detail.html', {'products': products, 'client_comments': client_comments})


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'cart.html', {'products': products})


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'checkout.html', {'products': products})


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        teamsays = TeamSays.objects.all()
        context = {
            'products': products,
            'teamsays': teamsays,
        }
        return render(request, 'about.html', context)


class BlogView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        blogs = Blog.objects.all()
        context = {
            'products': products,
            'blogs': blogs
        }
        return render(request, 'blog.html', context)


class ServicesView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        context = {
            'products': products,
            'client_comments': client_comments,
        }
        return render(request, 'services.html', context)


class ThankyouView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'thankyou.html', {'products': products})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'userprofile.html')


# Update and deletes
class ProductUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        return render(request, 'product_update.html', {'products': products})

    def post(self, request, id):
        product = Product.objects.get(id=id)
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.name = request.POST['name']
        product.price = request.POST['price']

        product.save()
        return redirect("shop")


class DeleteProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("shop")
