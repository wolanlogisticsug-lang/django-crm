from WOLANCRM.shortcuts import render

from common.utils.decorators import crm_staff_member_required
from crm.models import Company
from crm.models import Contact
from crm.models import Deal
from crm.models import Lead
from crm.models import Request


@crm_staff_member_required
def custom_dashboard(request):
    context = {
        "title": "Custom dashboard",
        "company_count": Company.objects.count(),
        "contact_count": Contact.objects.count(),
        "lead_count": Lead.objects.count(),
        "request_count": Request.objects.count(),
        "active_deal_count": Deal.objects.filter(active=True).count(),
    }
    return render(request, "crm/custom_dashboard.html", context)
