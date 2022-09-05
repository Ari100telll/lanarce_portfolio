def method_permission_classes(classes):
    """
    Function uses as a decorator for endpoint methods in DRF Views.
    It rewrites 'permission_classes' list.
    For example, View has a CRUD method. Only Delete required different permission.

    Add decorator for endpoint to achive it:
    @method_permission_classes([IsAdmin, DeleteOnly])
    def delete():
        ...
    """

    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)

        return decorated_func

    return decorator
