"""
Brief: Django models.py file.

Description: This file contains the models for the Django live app.

Author: Divij Sharma <divijs75@gmail.com>
"""

import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


TYPE_CHOICES = (
        (0x1 << 0, 'Open to All'),
        (0x1 << 1, 'Open within Ogranization'),
        (0x1 << 2, 'Open to Specific Users'),
    )

STATUS_CHOICES = (
        (0x1 << 0, 'Closed'),
        (0x1 << 1, 'Open'),
    )

SOCIAL_TYPE_CHOICES = (
        (0x1 << 0, 'Google OAuth'),
        (0x1 << 1, 'User List'),
    )


class Instance(models.Model):
    """
    Model for the Instance object.

    Fields:
    - user: User object, required.
    - instance_auth_type: Type of authentication for the instance, required.
    - name: Name of the instance, required.
    - description: Description of the instance, required.
    - instance_status: Status of the instance, required.
    - allowed_domains: List of allowed email domains for the instance.
    - created_at: Timestamp of the instance creation.
    - last_modified: Timestamp of the last modification of the instance.
    - hash: Unique hash for the instance object.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instance_auth_type = models.IntegerField(choices=TYPE_CHOICES, default=0x1 << 0)
    name = models.CharField(max_length=100)
    description = models.TextField()
    instance_status = models.IntegerField(choices=STATUS_CHOICES, default=0x1 << 1)
    allowed_domains = models.JSONField(null=True, blank=True, default=lambda: ["*"])
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    hash = models.CharField(max_length=16, unique=True, editable=False)

    def __str__(self):
        """
        Return the name of the instance object.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Save the instance object if the hash is not present (for POST requests).
        """
        if not self.hash:
            self.hash = uuid.uuid4().hex[:16]
        super().save(*args, **kwargs)

    def getInstance(hash, user):
        """
        Get the instance object by the hash if its accessible by the user.
        """
        return Instance.objects.get(hash=hash, user=user)

    def getExistingInstance(hash):
        """
        Get the instance object by the hash.
        """
        return Instance.objects.get(hash=hash)

    def getAllowedDomains(hash):
        """
        Get the allowed domains for the instance.
        """
        return Instance.objects.get(hash=hash).allowed_domains


class SocialUser(models.Model):
    """
    Model for the SocialUser object.

    Fields:
    - instance: Instance object, required.
    - user_social_type: Type of social user, required.
    - first_name: First name of the social user.
    - last_name: Last name of the social user.
    - username: Username of the social user, required.
    - password: Password of the social user, required.
    - has_voted: Flag indicating if the user has voted, defaults to False.
    - created_at: Timestamp of the social user creation.
    """
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    user_social_type = models.IntegerField(choices=SOCIAL_TYPE_CHOICES, default=0x1 << 1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100, blank=False, null=False, default='')
    password = models.CharField(max_length=128, blank=False, null=False)
    has_voted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['instance', 'username'], name='unique_instance_username')
        ]

    def __str__(self):
        """
        Return the name of the social user object.
        """
        return self.username

    def save(self, *args, **kwargs):
        """
        Save the social user object.
        """
        super().save(*args, **kwargs)
