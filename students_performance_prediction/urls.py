"""students_performance_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from students_performance_prediction import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^Search_StudentPerformance_DataSets/$', remoteuser.Search_StudentPerformance_DataSets, name="Search_StudentPerformance_DataSets"),
    re_path(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    re_path(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    re_path(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    re_path(r'^Search_Student_Performance/$', serviceprovider.Search_Student_Performance, name="Search_Student_Performance"),

    re_path(r'^View_All_StudentPerformance_Prediction_Details/$', serviceprovider.View_All_StudentPerformance_Prediction_Details, name="View_All_StudentPerformance_Prediction_Details"),
    re_path(r'^View_Student_Performance_Details/$', serviceprovider.View_Student_Performance_Details, name="View_Student_Performance_Details"),
    re_path(r'^View_Students_Assessments_Grades/$', serviceprovider.View_Students_Assessments_Grades, name="View_Students_Assessments_Grades"),
    re_path(r'^View_Search_Ratio/$', serviceprovider.View_Search_Ratio, name="View_Search_Ratio"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
