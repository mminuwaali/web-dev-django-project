from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_profile_upload(self, image) -> str:
    return f'profiles/{self.user.username}/{image}'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile = models.FileField(upload_to=user_profile_upload, blank=True, null=True)
    proffession = models.CharField(max_length=50, blank=True)
    reg_number = models.CharField(max_length=50, blank=True)
    team_member = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reg_number}"
