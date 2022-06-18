1. Install Django and Apps:
```shell
pip install Django==3.1.4
pip install django-phonenumber-field[phonenumbers]
```
2. Change Directory to Django---Hotel-Management-System/HMS and start the Shell:
```shell
python manage.py shell
```
* Then execute these, one by one:
```shell
from django.contrib.auth.models import Group, User
```

```shell
from accounts.models import Employee
```

```shell
Group.objects.create(name='admin')
```

```shell
Group.objects.create(name='manager')
```

```shell
Group.objects.create(name='receptionist')
```

```shell
Group.objects.create(name='staff')
```

```shell
Group.objects.create(name='guest')
```

```shell
user = User.createuser=User.objects.create_user('admin', password='admin123')
```

```shell
group = Group.objects.get(name="admin")
```

```shell
user.groups.add(group)
```

```shell
admin = Employee(user=user, salary=0)
```

```shell
admin.save()
```

## Exit the Shell
then :
python manage.py makemigrations
python manage.py migrate
```
Then, start the surver
```shell
python manage.py runserver
```
