# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'dbe.views.home', name='home'),
#     # url(r'^dbe/', include('dbe.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )


from django.conf.urls import *
from blog.models import *
from blog.views import PostView, Main, ArchiveMonth

urlpatterns = patterns("dbe.blog.views",
   (r"^post/(?P<dpk>\d+)/$"          , PostView.as_view(), {}, "post"),
   (r"^archive_month/(\d+)/(\d+)/$"  , ArchiveMonth.as_view(), {}, "archive_month"),
   (r"^$"                            , Main.as_view(), {}, "main"),
   # (r"^delete_comment/(\d+)/$"       , "delete_comment", {}, "delete_comment"),
   # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)