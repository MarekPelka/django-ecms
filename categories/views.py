from django.http import HttpResponse
from django.template import loader
from .models import Product, Application, Home, Contact

# Create your views here.
'''
def adetail(request, application_link):
    template = loader.get_template('product/adetail.html')
    try:
        prod = application.objects.get(link = product_link)
    except application.DoesNotExist:
        raise Http404("Product does not exist")
    context = {
        'product': prod
    }
    return HttpResponse(template.render(context, request))
'''
'''
def products(request, application_link):
def pdetail(request, application_link):
def applications(request, application_link):
def adetail(request, application_link):
'''
def home(request):
	template = loader.get_template('index.html')
	application_list = Application.objects.order_by('order')
	product_list = Product.objects.order_by('order')
	home = Home.objects.order_by('-id')[0]
	context = {
		'application_list': application_list,
		'product_list': product_list,
		'home': home
	}
	return HttpResponse(template.render(context, request))
#def contact(request, application_link):