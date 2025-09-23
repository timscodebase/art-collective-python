from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Profile

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates missing Profile objects for existing users.'

    def handle(self, *args, **options):
        self.stdout.write('Checking for missing profiles...')
        users_without_profiles = 0
        profiles_created = 0

        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
                profiles_created += 1
                users_without_profiles += 1
                self.stdout.write(self.style.SUCCESS(f'Created profile for user: {user.username}'))
            else:
                self.stdout.write(f'User {user.username} already has a profile.')

        if users_without_profiles == 0:
            self.stdout.write(self.style.SUCCESS('All existing users already have profiles. No action needed.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully created {profiles_created} missing profiles.'))
