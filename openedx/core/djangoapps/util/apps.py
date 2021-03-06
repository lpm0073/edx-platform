"""
Configuration for the openedx.core.djangoapps.util Django application
"""
from __future__ import absolute_import

from django.apps import AppConfig


class UtilConfig(AppConfig):
    """
    Configuration class for the openedx.core.djangoapps.util Django application
    """
    label = 'open_edx_util'
    name = 'openedx.core.djangoapps.util'
    verbose_name = 'Open edX Utilities'

    def ready(self):
        """
        Registers signal handlers at startup.
        """
        import openedx.core.djangoapps.util.signals  # pylint: disable=unused-variable
