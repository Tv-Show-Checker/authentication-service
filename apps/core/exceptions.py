from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class TooManyRequest(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = _('Too many failed login attempts try again later')
    default_code = 'too_many_requests'
