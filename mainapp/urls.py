from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    
    
    #REGISTER
    path('register/',views.registerUser,name='register'),
    
    
    
    #TEST
    path('test/',views.test,name='test'),
    
    
    
    #EMP
    path('e-table/',views.employeetable,name='e_table'),
    path('e-create/',views.createEmployee,name='e_create'),
    path('e-update/<str:pk>',views.updateEmp,name='e_update'),
    path('e-delete/<str:pk>',views.empDelete,name='e_delete'),
    
    
    
    #PRODUCT
    path('p-table/',views.productTable,name='p_table'),
    path('p-create/',views.createProduct,name='p_create'),
    path('p-update/<str:pk>',views.updatePro,name='p_update'),
    path('p-delete/<str:pk>',views.proDelete,name='p_delete'),
    
    
    #MEVALAR
    path('f-table/',views.fruitTable,name='f_table'),
    path('f-create/',views.createFruit,name='f_create'),
    path('f-update/<str:pk>',views.updateFruit,name='f_update'),
    path('f-delete/<str:pk>',views.fruitDelete,name='f_delete'),
    
    
    #GOSHT
    path('m-table/',views.meatTable,name='m_table'),
    path('m-create/',views.createMeat,name='m_create'),
    path('m-update/<str:pk>',views.updateMeat,name='m_update'),
    path('m-delete/<str:pk>',views.meatDelete,name='m_delete'),
    
    
    #FUTBOLKA
    path('fu-table/',views.futbolkaTable,name='fu_table'), 
    
    
    #KOYLAK
    path('k-table/',views.koylakTable,name='k_table'), 
    
    
    #KEPKA
    path('ke-table/',views.kepkaTable,name='ke_table'), 
    
    
    #NON
    path('n-table/',views.nonTable,name='n_table'), 
    path('n-create/',views.createNon,name='n_create'),
    path('n-update/<str:pk>',views.updateNon,name='n_update'),
    path('n-delete/<str:pk>',views.nonDelete,name='n_delete'),
    
    
    #SUV
    path('s-table/',views.suvTable,name='s_table'), 
    path('s-create/',views.createSuv,name='s_create'),
    path('s-update/<str:pk>',views.updateSuv,name='s_update'),
    path('s-delete/<str:pk>',views.suvDelete,name='s_delete'),
    
    
    #MUZQAYMOQ
    path('muz-table/',views.muzTable,name='muz_table'), 
    path('muz-create/',views.createMuz,name='muz_create'),
    path('muz-update/<str:pk>',views.updateMuz,name='muz_update'),
    path('muz-delete/<str:pk>',views.muzDelete,name='muz_delete'),
    
    
    #SHOKOLAD
    path('sh-table/',views.shokolodTable,name='sh_table'),
    path('sh-create/',views.createShokolod,name='sh_create'),
    path('sh-update/<str:pk>',views.updateShokolod,name='sh_update'),
    path('sh-delete/<str:pk>',views.shokolodDelete,name='sh_delete'),
    
    
    #SUT
    path('sut-table/',views.milkTable,name='sut_table'),  
    
    
    #UN
    path('un-table/',views.flourTable,name='un_table'),
    
    
    #SABZAVOTLAR
    path('sab-table/',views.vegetableTable,name='sab_table'),  
    
    
    
    #SOAT
    path('soat-table/',views.watchTable,name='soat_table'),  
    path('soat-table/about/',views.watch_about,name='about'),
    
    
    #OYOQ KIYIM 
    path('sho-table/',views.shoesTable,name='sho_table'),
    
    #VENTROVKA       
    path('v-table/',views.ventrovkaTable,name='v_table'),   
    
    
    #JILET     
    path('j-table/',views.jiletTable,name='j_table'),   
    
    
    
    #PAYPOQ   
    path('po-table/',views.paypoqTable,name='po_table'),     
    
    
    
    #CHARTS
    path('chart/',views.chartjs,name='chartjs'),
    
    
    #FORMS
    path('forms/',views.forms,name='forms'),       
]