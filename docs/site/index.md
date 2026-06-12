
# [<img src="img/WolanCRM_logo.png" alt="WOLANCRM CRM Screenshot" width="50px" align="center" style="float: center"/>](https://github.com/WOLANCRM/WolanCRM/){target="_blank"} Welcome to WolanCRM Documentation

[WOLANCRM CRM](https://github.com/WOLANCRM/WolanCRM/){target="_blank"} (client relationship software) is an open source application with web interface.  
This CRM is based on the [WOLANCRM Admin site](https://docs.WOLANCRMproject.com/en/dev/ref/contrib/admin/){target="_blank"} and is written in the [Python](https://www.python.org/){target="_blank"} programming language.

[<img src="img/WolanCRM_deals_screenshot_2x1v2.png" alt="WOLANCRM CRM Screenshot" align="center" style="float: center"/>](img/WolanCRM_deals_screenshot_2x1v2.png){target="_blank"}
<hr/>
<div align="center">
<a class="btn button" href="/en/latest/installation/">CRM installation</a>
<a class="btn button" href="/en/latest/introduction/">User guide</a>
</div><br>

WOLANCRM CRM offers a comprehensive CRM solution and consists of the following core applications:

- __TASKS__ ([CRM task management](https://WOLANCRM.github.io/info/features/tasks-app-features/){target="_blank"}: management of tasks, projects, memos)
- __CRM__ ([CRM Application](https://WOLANCRM.github.io/info/features/crm-app-features/){target="_blank"}: management of leads, contacts, companies, deals, products, etc.)
- __ANALYTICS__ ([CRM Analytics software](https://WOLANCRM.github.io/info/features/analytics-app-features/){target="_blank"}: sales funnel and other seven reports)
- __MASS MAIL__ ([CRM email marketing](https://WOLANCRM.github.io/info/features/massmail-app-features/){target="_blank"}: free mass email sender)

The CRM task management does not require configuration and allows individual users or teams to work with the following objects and objects associated with them:

- [Tasks](tasks_section.md#tasks) -> Subtasks
- Projects -> Tasks -> Subtasks
- [Memos](tasks_section.md#memos) (office memos) -> Projects or Tasks 

Each instance of these objects also has integration with:

- [<img src="icons/chat-left-text.svg" alt="Chat icon" style="vertical-align: sub;" width="17" height="17"> Chat](tasks_section.md#chat-in-objects)
- <span style="vertical-align: baseline"><img src="icons/tags.svg" alt="tag icon" width="17" height="17"></span>  Tags
- <span style="vertical-align: baseline"><img src="icons/alarm.svg" alt="alarm icon" width="17" height="17"></span> Remainders
- [<img src="icons/paperclip.svg" alt="paperclip icon" style="vertical-align: sub;" width="17" height="17"> Files](introduction.md#file-object)

Notifications within CRM system and to Email are also available.  
All CRM users have access to this application by default.

Access to the rest of the WOLANCRM CRM applications is only available to users with the appropriate [roles](adding_crm_users.md#user-groups-roles), such as [sales managers](guide_for_sales_manager.md), [company executives](guide_for_company_executives.md), etc.  
To use all the features of these applications, you need to set up __CRM software integration__:

- with your company's websites
- with your company's mailboxes and sales managers' mailboxes
- if necessary:
    - with the service of receiving [currency](currencies.md) exchange rates
    - with VoIP telephony service 

---
