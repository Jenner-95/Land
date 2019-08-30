from django.urls import path
from estate import views

app_name = 'estate'

urlpatterns = [
    path('estate_detail/<int:user_id>/', views.estate_detail, name='estate_detail'),
    path('estate_add/<int:user_id>/', views.create_estate_form, name='estate_add'),
    path('estate_edit/<int:estate_id>/<int:user_id>/', views.edit_estate_form, name='estate_edit'),
    path('estate_delete/<int:estate_id>/<int:user_id>/', views.delete_estate, name='estate_delete'),
    path('plot_detail/<int:estate_id>/<int:user_id>/', views.plot_detail, name='plot_detail'),
    path('plot_add/<int:estate_id>/<int:user_id>/', views.create_plot_form, name='plot_add'),
    path('plot_edit/<int:plot_id>/<int:user_id>/', views.edit_plot_form, name='plot_edit'),
    path('plot_delete/<int:plot_id>/<int:estate_id>/<int:user_id>/', views.delete_plot, name='plot_delete'),
    path('tree_detail/<int:plot_id>/<int:user_id>/', views.tree_detail, name='tree_detail'),
    path('tree_add/<int:plot_id>/<int:user_id>/', views.create_tree_form, name='tree_add'),
    path('tree_edit/<int:tree_id>/<int:user_id>/', views.edit_tree_form, name='tree_edit'),
    path('tree_delete/<int:tree_id>/<int:plot_id>/<int:user_id>/', views.delete_tree, name='tree_delete'),
]