
class KongError(Exception):

    def __init__(self, message=None, context=None):
        super(KongError, self).__init__(message)
        self.message = message
        self.context = context


class ArgumentError(ValueError, KongError):
    pass


class HttpError(KongError):
    pass


class ResourceNotFound(KongError):
    pass


class AuthenticationError(KongError):
    pass


class ServerError(KongError):
    pass


class BadGatewayError(KongError):
    pass


class ServiceUnavailableError(KongError):
    pass


class BadRequestError(KongError):
    pass


class RateLimitExceeded(KongError):
    pass


class MultipleMatchingUsersError(KongError):
    pass


class UnexpectedError(KongError):
    pass


class TokenUnauthorizedError(KongError):
    pass


error_codes = {
    'unauthorized': AuthenticationError,
    'forbidden': AuthenticationError,
    'bad_request': BadRequestError,
    'action_forbidden': BadRequestError,
    'missing_parameter': BadRequestError,
    'parameter_invalid': BadRequestError,
    'parameter_not_found': BadRequestError,
    'not_found': ResourceNotFound,
    'service_unavailable': ServiceUnavailableError,
}
