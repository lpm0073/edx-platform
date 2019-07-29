"""
Permission definitions for the content_type_gating djangoapp
"""

from bridgekeeper import perms
from lms.djangoapps.courseware.rules import HasStaffRolesRule

perms['feature_based_enrollments.bypass_fbe'] = HasStaffRolesRule()

