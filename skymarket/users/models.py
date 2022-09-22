from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser):
    ADMIN = 'admin'
    USER = 'user'
    ROLES = [
        (ADMIN, ADMIN),
        (USER, USER)
    ]

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя, максимально 50 символов",
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите имя, максимально 50 символов",
    )

    email = models.EmailField(
        unique=True,
        help_text="Укажите электронную почту",
    )

    phone = models.CharField(
        max_length=25,
        verbose_name="Номер телефона",
        help_text="Укажите телефон для связи",

    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default=USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя",
    )

    is_active = models.BooleanField(
        verbose_name="Аккаунт активен",
        help_text="Укажите, активен ли аккаунт"
    )

    image = models.ImageField(upload_to='user_avatars/', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == User.ADMIN

    @property
    def is_user(self):
        return self.role == User.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']

    def __str__(self):
        return self.email
