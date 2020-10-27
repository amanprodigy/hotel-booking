class AlreadyRegisteredError(Exception):
    message = 'User is already registered'


class BookingRequirementNotMetException(Exception):
    message = 'Not enough rooms vacant to meet this booking requirement'
