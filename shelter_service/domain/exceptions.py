class UserAlreadyExists(Exception):
    """Exception, when user with same email has already existed"""
    pass

class MissingFileExtension(Exception):
    """Exception, when image doesnt consist some extension"""
    pass