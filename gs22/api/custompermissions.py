from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET': #change this method to post and fire a get request
            return True
        return False
        