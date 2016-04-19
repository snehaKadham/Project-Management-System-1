from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$',views.rendersystem,name = 'polls'),
		url(r'^dashboard',views.renderdashboard,name='dashboard'),
        url(r'^notifications',views.rendernotifications,name='notifications'),
		url(r'^table1',views.rendertable1,name = 'table1'),
		url(r'^table2',views.rendertable2,name = 'table2'),
		url(r'^table',views.rendertable,name = 'table'),
		url(r'^template',views.rendertemplate,name = 'template'),
		url(r'^user',views.renderuser,name = 'user'),
        url(r'^add_project',views.renderadd_project,name = 'add_project'),
		url(r'^index',views.renderindex,name = 'index'),
		url(r'^project_view',views.renderproject_details_view,name = 'project_view'),	#make seperate functions when you need to render
		url(r'^others_view',views.renderproject_details_view,name = 'others_view'),		#files also
		url(r'^previous_projects_view',views.renderproject_details_view,name = 'previous_projects_view'),
		url(r'^txt-editor',views.txtEditor),
		url(r'^chat_page$', views.chat_page, name = "chat_page"),
		url(r'^chat_table$', views.chat_table, name = "chat_table"),
		url(r'^AJAX$', views.tryAjax, name = "tryAjax"),
		url(r'^guest',views.renderguest,name = 'guest'),
		url(r'^newtable',views.rendernewtable,name = 'newtable'),
		url(r'^logout',views.renderlogout,name = 'logout'),
		]
