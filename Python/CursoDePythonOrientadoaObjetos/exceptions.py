class LibraryError(Exception):
    pass

class TitleInvalidError(LibraryError):
    pass

class BookNotAvailableError(LibraryError):
    pass