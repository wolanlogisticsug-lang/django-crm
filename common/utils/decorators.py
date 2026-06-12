from django.contrib.admin.views.decorators import staff_member_required


def crm_staff_member_required(view_func=None):
    return staff_member_required(view_func, login_url='site:login')
