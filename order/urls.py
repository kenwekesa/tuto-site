from django.contrib import admin
from django.urls import path
from . import views as mainviews

from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

admin.site.index_template = 'dashboards/admin_dash.html'
admin.autodiscover()

urlpatterns = [
    path('place_order', mainviews.place_order_view, name="placeorder"),
    path('admin_dashboard', mainviews.admin_dash_view, name="admin-dashboard"),
    path('orders_view', mainviews.orders_view, name="view-orders"),
    path('review_and_pay/<slug:slug>', mainviews.review_and_pay_view, name="review-and-pay"),

    path('update_payment', mainviews.update_payment, name="update-payment"),
    
    path('view_order/<slug:slug>', mainviews.view_order_view, name="view-order"),
    path('order_placed/<slug:slug>', mainviews.order_placed_view, name="order-placed"),



    path('login', mainviews.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'dashboards/logged_out.html'), name='logout'),


    #Search
    path("search/", mainviews.search_orders_by_name, name="search-by-name" ),

  


]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)