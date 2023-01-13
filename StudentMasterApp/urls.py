from django.urls import path

from StudentMasterApp import views

urlpatterns=[
    path('',views.home_fun,name='home'),
    path('stdlogin',views.std_login_fun,name='stdlogin'),
    path('stdregister',views.std_register_fun,name='stdreg'),
    path('mst_login',views.mst_login_fun,name='mstlogin'),
    path('mst_register',views.mst_register_fun,name='mstreg'),
    path('taskview',views.task_view_fun,name='taskview'),
    path('taskassign',views.task_assign_fun,name='taskassign'),
    path('readslogin',views.read_student_login_fun),
    path('readmlogin',views.read_master_login_fun),
    path('readdata1',views.read_student_register_fun),
    path('readdata',views.read_master_register_fun),
    path('createtask',views.create_task_fun),
    path('log_out',views.logout_fun,name='log_out'),
    path('solve/<int:id>',views.solve_fun,name='solve')
]