from functools import wraps
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import Permission
from vet.urls import *
import logging

# decorator to set permission of vets
def vet_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # checks that the user is active and has the 'is_vet' attribute set to True
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_vet,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    # If a function is provided, apply the decorator
    if function:
        return actual_decorator(function)
    return actual_decorator

# decorator to set permission of owners
def owner_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # checks that the user is active and has the 'is_owner' attribute set to True
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_owner,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    # If a function is provided, apply the decorator
    if function:
        return actual_decorator(function)
    return actual_decorator

#decorator to set permission of admin vets
def custom_permission_required(perm_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            full_perm_name = f"accounts.{perm_name}"
            #Verify that the request user has the permission added to his account
            if request.user.has_perm(full_perm_name):
                return view_func(request, *args, **kwargs)
            else:
                #redirects to a basic error page because dont have permissions
                return HttpResponseForbidden("You're not supposed to be here, you don't have the necessary permissions")
        return _wrapped_view
    return decorator