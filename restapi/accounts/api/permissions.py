from rest_framework import permissions

class BlacklistPermission(permissions.BasePermission):
    def has_permission(self,request,view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted

class AnonPermissionOnly(permissions.BasePermission):
    '''
    Non-Authenticated Users Only
    '''
    message = 'You are already authentciated pls log out and try again'
    def has_permission(self, request, view):
        return not request.user.is_authentciated



class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Object level permission
    '''
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user