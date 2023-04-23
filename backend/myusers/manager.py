from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        if not email:
            raise ValueError('Email must be present')
        if not username:
            raise ValueError('Username must be present')
        if not first_name:
            raise ValueError('Firstname must be present')
        if not last_name:
            raise ValueError('Lastname must be present')

        myuser = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        myuser.set_password(password)
        myuser.save(self._db)
        return myuser

    def create_superuser(self, email, username, first_name, last_name, password):
        superuser = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.is_staff = True

        superuser.save(using=self._db)
        return superuser
