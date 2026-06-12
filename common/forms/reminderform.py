from WOLANCRM.forms import ModelForm
from WOLANCRM.forms import Textarea

from common.models import Reminder


class ReminderForm(ModelForm):

    class Meta:
        model = Reminder
        fields = '__all__'
        widgets = {
            'subject': Textarea(attrs={'cols': 80, 'rows': 2}),
            'description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
