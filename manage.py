#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('WOLANCRM_SETTINGS_MODULE', 'webcrm.settings')
    os.environ.setdefault('WOLANCRM_RUNSERVER_HIDE_WARNING', 'true')
    try:
        from WOLANCRM.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import WOLANCRM. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

