from tortoise import Model, fields

from ..fields import CITextField, CustomTextField


class AbstractBaseUser(Model):
    """
        Abstract Class for User and Guest User Models
        Provides all the fields for User Tables

    """

    serializable_keys = {'username', 'suspended', 'verified', 'is_guest', 'email', 'number', 'number_verified',
                         'is_migrated', 'email_verified', 'external_id', 'roles', 'properties', 'updated_on',
                         'authentication_token_expiry', 'suspended_on', 'authentication_token',
                         'created_on', 'last_login', 'properties_new'}

    username = CITextField(max_length=100, pk=True)
    passkey = fields.CharField(max_length=100, null=True)
    salt = fields.TextField(null=True)
    suspended = fields.BooleanField(default=False)
    verified = fields.BooleanField(default=False)
    update_token = fields.TextField(null=True)
    update_token_expiry = fields.BigIntField(null=True)
    authentication_token = fields.TextField(null=True)
    authentication_token_expiry = fields.IntField(null=True)
    suspended_on = fields.BigIntField(null=True)
    last_login = fields.BigIntField(null=True)
    created_on = fields.BigIntField(null=False)
    updated_on = fields.BigIntField(null=False)
    is_guest = fields.BooleanField(default=False)
    email = CITextField(max_length=100, unique=True, null=True)
    number = fields.CharField(max_length=100, unique=True, null=True)
    number_verified = fields.BooleanField(default=False)
    is_migrated = fields.BooleanField(default=False)
    email_verified = fields.BooleanField(default=False)
    referral_code = CustomTextField(unique=True, null=True)
    referred_by = CITextField(max_length=100, null=True)

    class Meta:
        abstract = True

