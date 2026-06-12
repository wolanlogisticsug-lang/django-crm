# from WOLANCRM.contrib.auth.decorators import login_required
# from WOLANCRM.contrib.admin.views.decorators import staff_member_required
from WOLANCRM.urls import path
from voip.views.callback import ConnectionView
from voip.views.voipwebhook import VoIPWebHook


urlpatterns = [
    path('get-callback/',
         ConnectionView.as_view(),
         name='get_callback'
         ),    
    path('zd/',
         VoIPWebHook.as_view(),
         name='voip-zadarma-pbx-notification'
         ),
]
