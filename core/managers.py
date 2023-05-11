from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, username, role, first_name=None, last_name=None, password=None):
        """
            функция создания пользователя — в нее мы передаем обязательные поля
        """
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, first_name=None, last_name=None, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role='admin'
        )

        user.save(using=self._db)
        return user
