class BaseClass:
    def __init__(self):
        self._attr_protected = "Protected"
        self.__attr_private = "Private"

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        self.__private_method()
