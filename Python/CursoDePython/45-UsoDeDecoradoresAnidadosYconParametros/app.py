def check_access(required_role):
    def decorator(func):
        def wrapper(user):
            if user.get("role") == required_role:
                return func(user)
            else:
                print("You don't have access")

        return wrapper

    return decorator


def log(func):
    def wrapper(user):
        print(f'Register action for User {user["name"]}')
        return func(user)
    return wrapper


@check_access("admin")
@log
def delete_user(user):
    print(f'User {user["name"]} deleted')

admin = {"name": "Carlos", "role": "admin"}
user = {"name": "Juan", "role": "user"}

delete_user(admin)
delete_user(user)