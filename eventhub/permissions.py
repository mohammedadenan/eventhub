from rest_framework.permissions import BasePermission


class IsOrganizer(BasePermission):
    '''only Autharized Organizer Can Create Event'''

    def has_permission(self, request,view):
        return bool(request.user.is_authenticated and request.user.is_staff)

class IsCustomer(BasePermission):
    '''Only Non_Admin Are Aloowed'''

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_staff==False)