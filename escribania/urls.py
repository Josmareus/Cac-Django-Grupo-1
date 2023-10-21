from django.urls import path
from . import views


urlpatterns=[

    # URLs para el Escribano
    path('crear_escribano/', views.CrearEscribanoView.as_view(), name='crear_escribano'),
    path('listar_escribanos/', views.ListarEscribanosView.as_view(), name='listar_escribanos'),
    path('actualizar_escribano/<int:pk>/', views.ActualizarEscribanoView.as_view(), name='actualizar_escribano'),
    path('eliminar_escribano/<int:pk>/', views.EliminarEscribanoView.as_view(), name='eliminar_escribano'),

    #para ActoJuridico
    path('crear_acto_juridico/', views.CrearActoJuridicoView.as_view(), name='crear_acto_juridico'),
    path('listar_actos_juridicos/', views.ListarActosJuridicosView.as_view(), name='listar_actos_juridicos'),
    path('actualizar_acto_juridico/<int:pk>/', views.ActualizarActoJuridicoView.as_view(), name='actualizar_acto_juridico'),
    path('eliminar_acto_juridico/<int:pk>/', views.EliminarActoJuridicoView.as_view(), name='eliminar_acto_juridico'),

    #para Escrituras
    path('crear_escrituras/', views.CrearEscrituraView.as_view(), name='crear_escritura'),
    path('listar_escrituras/', views.ListarEscrituraView.as_view(), name='listar_escrituras'),
    path('actualizar_escritura/<int:pk>/', views.ActualizarEscrituraView.as_view(), name='actualizar_escritura'),
    path('eliminar_escritura/<int:pk>/', views.EliminarEscrituraView.as_view(), name='eliminar_escritura'),
]