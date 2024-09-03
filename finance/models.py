from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'user_type'
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60, blank=True, null=True)
    user = models.ManyToManyField(User)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'organization'

    def __str__(self):
        return f'{self.id}-{self.name}'
#     user_organization = models.ManyToManyField(User, through='UserOrganization',
#                                                through_fields=['user_id', 'organization_id'])
#
# #
# class UserOrganization(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
