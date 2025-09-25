from django.urls import reverse
from django.utils.html import format_html


def breadcrumb_context(request):
    """
    Add breadcrumb navigation to all templates.
    """
    breadcrumbs = []
    path = request.path
    
    # Always start with home
    breadcrumbs.append({
        'name': 'Home',
        'url': reverse('landing:home')
    })
    
    # Gallery section breadcrumbs
    if path.startswith('/gallery/'):
        breadcrumbs.append({
            'name': 'Gallery',
            'url': reverse('gallery:image_list')
        })
        
        if 'artists' in path:
            breadcrumbs.append({
                'name': 'Artists',
                'url': reverse('gallery:gallery_list')
            })
        elif 'upload' in path:
            breadcrumbs.append({
                'name': 'Upload Image',
                'url': reverse('gallery:upload_image')
            })
        elif '/user/' in path:
            # Extract username from path for user profiles
            username = path.split('/user/')[-1].rstrip('/')
            if username:
                breadcrumbs.append({
                    'name': f"Artist: {username}",
                    'url': request.path
                })
        elif path.count('/') > 2:  # Likely an image detail page
            breadcrumbs.append({
                'name': 'Image Detail',
                'url': request.path
            })
    
    # Chat section breadcrumbs
    elif path.startswith('/chat/'):
        breadcrumbs.append({
            'name': 'Chat',
            'url': reverse('chat:room_list')
        })
        
        if path.count('/') > 2:  # Likely in a specific room
            breadcrumbs.append({
                'name': 'Chat Room',
                'url': request.path
            })
    
    # Accounts section breadcrumbs
    elif path.startswith('/accounts/'):
        breadcrumbs.append({
            'name': 'My Account',
            'url': reverse('accounts:dashboard')
        })
        
        if 'change-username' in path:
            breadcrumbs.append({
                'name': 'Change Username',
                'url': request.path
            })
        elif 'update-profile' in path:
            breadcrumbs.append({
                'name': 'Update Profile', 
                'url': request.path
            })
        elif 'manage-photos' in path:
            breadcrumbs.append({
                'name': 'Manage Photos',
                'url': request.path
            })
        elif 'change-theme' in path:
            breadcrumbs.append({
                'name': 'Change Theme',
                'url': request.path
            })
    
    # Authentication breadcrumbs
    elif path in ['/login/', '/signup/', '/password_change/', '/password_change/done/']:
        if 'login' in path:
            breadcrumbs.append({'name': 'Login', 'url': request.path})
        elif 'signup' in path:
            breadcrumbs.append({'name': 'Sign Up', 'url': request.path})
        elif 'password_change' in path:
            breadcrumbs.append({'name': 'Change Password', 'url': request.path})
    
    return {
        'breadcrumbs': breadcrumbs if len(breadcrumbs) > 1 else []
    }


def site_context(request):
    """
    Add site-wide context variables.
    """
    return {
        'site_name': 'Artist Collective',
        'current_section': _get_current_section(request),
    }


def _get_current_section(request):
    """Helper function to determine the current site section."""
    path = request.path
    
    if path.startswith('/gallery/'):
        return 'gallery'
    elif path.startswith('/chat/'):
        return 'chat'  
    elif path.startswith('/accounts/'):
        return 'accounts'
    elif path in ['/login/', '/signup/', '/password_change/', '/password_change/done/']:
        return 'auth'
    else:
        return 'home'