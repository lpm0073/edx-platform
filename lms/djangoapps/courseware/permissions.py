"""
Permission definitions for the courseware djangoapp
"""

from bridgekeeper import perms
from .rules import HasAccessRule

PERM_VIEW_COURSE_HOME = 'courseware.view_course_home'
PERM_VIEW_COURSEWARE = 'courseware.view_courseware'

perms[PERM_VIEW_COURSE_HOME] = HasAccessRule('load')
perms[PERM_VIEW_COURSEWARE] = HasAccessRule('load')
