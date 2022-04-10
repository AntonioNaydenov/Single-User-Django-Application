from django.urls import path

from expenses_site.web.views import show_index, create_expense_page, edit_expense_page, delete_expense_page, \
    show_profile, edit_profile_page, delete_profile_page, create_profile

urlpatterns = (
    path('', show_index, name='index'),

    path('create/', create_expense_page, name='create expense'),
    path('edit/<int:pk>/', edit_expense_page, name='edit expense'),
    path('delete/<int:pk>/', delete_expense_page, name='delete expense'),

    path('profile/', show_profile, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile_page, name='edit profile'),
    path('profile/delete/', delete_profile_page, name='delete profile'),
)
