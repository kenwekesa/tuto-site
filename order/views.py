from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import OrderForm, ClientForm
from django.contrib import messages
from .models import Order, Client

from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate

import json
# Create your views here.



def login_view(request):
    #context = {'posts': Post.objects.all()}
  
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    return redirect("admin-dashboard")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="dashboards/admin_login.html", context={"login_form":form})


def homepage(request):
    #context = {'posts': Post.objects.all()}
    return render(request, 'order/index.html')#,context)



@login_required
def admin_dash_view(request):
    #context = {'posts': Post.objects.all()}
    context = {}
    orders = Order.objects.all()
    context['orders'] = orders

	
    return render(request, 'dashboards/admin_dash.html',context)#,context)

@login_required
def orders_view(request):
    #context = {'posts': Post.objects.all()}
    context = {}
    orders = Order.objects.all()
    context['orders'] = orders

	
    return render(request, 'dashboards/orders_list.html',context)#,context)


@login_required
def view_order_view(request,slug):


    #fetch that specified order
    try:
        order = Order.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('view-order', slug=slug)

    #fetch all the products - related to this invoice
    

    
            



    context = {}
    context['order'] = order
    

    return render(request, 'dashboards/view_order.html', context)


#@login_required
def order_placed_view(request,slug):


    #fetch that specified order
    try:
        order = Order.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('view-order', slug=slug)

    #fetch all the products - related to this invoice
    

    
            



    context = {}
    context['order'] = order
    

    return render(request, 'order/order_placed_view.html', context)

def place_order_view(request):
    #context = {'posts': Post.objects.all()}

    #--------------------------------------------------
    if request.method == 'POST':
     
        form = OrderForm(request.POST, request.FILES)
        client_form = ClientForm(request.POST)
       
        if form.is_valid() and client_form.is_valid():
            
            #messages.success(request, f'Order created successfully')
            request.session['order_data'] = json.dumps(form.cleaned_data, default=str)
            request.session['client_data'] = client_form.cleaned_data

            client = client_form.save
            form.client = client

            orders = form.save
            
            return render(request, 'order/review_order.html',{'orders':orders, 'order': form.cleaned_data, 'client': client_form.cleaned_data,'form':form,'client_form':client_form})
    
    else:
        form = OrderForm()
        client_form=ClientForm()
       

    
    return render(request=request, template_name="order/place_order.html", context={"form":form, "client_form": client_form})
    #---------------------------------------------------



def review_and_pay_view(request, slug):
    #context = {'posts': Post.objects.all()}

    #--------------------------------------------------
    order = Order.objects.get(slug = slug)
    order_data = json.loads(request.session['order_data'])
    client_data = request.session['client_data']

    """client=Client(first_name=client_data['first_name'],last_name=client_data['last_name'], emailAddress=client_data['emailAddress'])
    
    order =Order(assignment_file=order_data["assignment_file"], topic = order_data["topic"],subject=order_data['subject'],
    number_of_pages= order_data['number_of_pages'],powerpoint_slides=order_data['powerpoint_slides'],
    number_of_sources=order_data['number_of_sources'],client=client,deadline=order_data['deadline'], assignment_details= order_data['assignment_details'],payment_made=1)
    
    client.save()
    order.save()
    """
    del request.session['order_data']
    del request.session['client_data']
   
    
    return redirect("order-placed",order.slug)

    
       

    
   
    #---------------------------------------------------


    #------------------------PAYPAL PAYMENT -------------------------

"""def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
    'business': settings.PAYPAL_RECEIVER_EMAIL,
    'amount': '%.2f' % order.total_cost().quantize(
        Decimal('.01')),
    'item_name': 'Order {}'.format(order.id),
    'invoice': str(order.id),
    'currency_code': 'USD',
        notify_url': 'http://{}{}'.format(host,
                                        reverse('paypal-ipn')),
    'return_url': 'http://{}{}'.format(host,
                                        reverse('payment_done')),
    'cancel_return': 'http://{}{}'.format(host,
                                            reverse('payment_cancelled')),
         }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'ecommerce_app/process_payment.html', {'order': order, 'form': form})
"""


def handle_uploaded_files(f):
    with open(f'uploaded/folder/path/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)







#-------------------------------Handle search here---------------------------------------
def search_orders_by_name(request):

	if request.method == "GET":
		search_text = request.GET['search_text']
		if search_text is not None and search_text != u"":
			search_text = request.GET['search_text']
			orders = Order.objects.filter(status__icontains = search_text)
           
		else:
			orders = []


		data = orders.values()
	

		return render(request, 'order/search_results.html', {"orders": orders})

