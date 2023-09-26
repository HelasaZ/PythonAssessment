from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create test users'

    def handle(self, *args, **kwargs):
        # Create a user with user_type 'user'
        User.objects.create_user('user', 'test@test.com', 'password')
        self.stdout.write(self.style.SUCCESS('User "user1" created successfully.'))

        # Create a user with user_type 'manager'
        User.objects.create_user('manager1', 'breakit2270@gmail.com', 'x8dXF#5JDScar5QE')
        self.stdout.write(self.style.SUCCESS('User "manager1" created successfully.'))
