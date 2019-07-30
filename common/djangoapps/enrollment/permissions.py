"""
Permission definitions for the courseware djangoapp
"""

from bridgekeeper import perms
from .rules import HasAccessRule

PERM_ENROLL_IN_COURSE = 'enrollment.enroll_in_course'

perms[PERM_ENROLL_IN_COURSE] = HasAccessRule('enroll')
