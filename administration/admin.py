# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from django.contrib import admin

# Register your models here.
from model.models import CMDB,Deploylog,Deploy,DeployItems,Approve
# admin.site.register(Article)
# admin.site.register(Reporter)
admin.site.register(CMDB)
admin.site.register(Deploy)
admin.site.register(DeployItems)
admin.site.register(Deploylog)
admin.site.register(Approve)

if __name__ == '__main__':

    print sys.getdefaultencoding()