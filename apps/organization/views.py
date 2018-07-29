from django.shortcuts import render
from django.views.generic import View

from .models import *


# Create your views here.

class OrgView(View):
    '''
    课程机构列表功能
    '''

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        # 城市
        all_citys = CityDict.objects.all()

        return render(request, 'org-list.html', locals())
