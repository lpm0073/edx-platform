"""
Permission definitions for the course_duration_limits djangoapp
"""

from bridgekeeper import perms
from lms.djangoapps.courseware.rules import HasStaffRolesRule

perms['feature_based_enrollments.bypass_fbe'] = HasStaffRolesRule()
