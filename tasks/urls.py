from WOLANCRM.urls import path

from common.utils.decorators import crm_staff_member_required
from tasks.views.create_completed_subtask import create_completed_subtask
from tasks.views.create_completed_subtask import email_subtask_completion
from tasks.views.task_completed import task_completed


urlpatterns = [
    path(
        "create-completed-subtask/<int:object_id>/",
        crm_staff_member_required(create_completed_subtask),
        name="create_completed_subtask"
    ),
    path(
        'email-subtask_completed/<slug:token>/<int:object_id>/',
        email_subtask_completion,
        name='email-subtask_completed'
    ),
    path(
        'task_completed/<slug:token>/<int:object_id>/',
        task_completed,
        name='task_completed'
    )
]
