from django.urls import path
from . import views,empviews,deptviews

urlpatterns=[

    # Homepage url
    path('',views.homepage, name='homepage'),

    # signup/login urls
    path('adminsignup/', views.admin_signup, name='adminsignup'),
    path('empsignup/', views.signup_page, name='empsignup'),
    path('login/', views.user_login, name='login'),

    # Display details url
    path('list/', empviews.list, name='list'),

    # employee_table urls
    path('empdetails/', empviews.emp_details, name='empdetails'),#add page
    path('empmanage/', empviews.employee_manage, name='empmanage'),#view page
    path('empedit/<str:emp_email>', empviews.employee_edit, name='empedit'),#editpage
    path('empdelete/<str:emp_email>', empviews.employee_delete, name='empdelete'),#deletepage

    # Department_table urls
    path('deptdetails/',deptviews.dept_details, name='deptdetails'),#add page
    path('deptmanage/', deptviews.dept_manage, name='deptmanage'),#view page
    path('deptedit/<int:dept_id>', deptviews.dept_edit, name='deptedit'),#Edit page
    path('deptdelete/<int:dept_id>', deptviews.dept_delete, name='deptdelete'),#Delete page
]