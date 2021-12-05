import logging
import apiclient
import ssl
import time

logger = logging.getLogger(__name__)

class GDriveError(Exception):
    pass

class GDriveNetworkError(RuntimeError):
    pass

def retryer(max_retries=10, timeout=2):
    logger.debug(f'max_retries: {max_retries}, timeout: {timeout}')
    def decorator(func):
        @wraps(func)
        def retry(*args, **kwargs):
            network_exceptions = (
                apiclient.errors.HttpError,
                ssl.SSLEOFError,
            )
            for i in range(max_retries):
                logger.debug(f'attempt: {i}')
                try:
                    result = func(*args, **kwargs)
                except network_exceptions:
                    time.sleep(timeout)
                    continue
                else:
                    return result
            else:
                raise GDriveNetworkError('error making connection')
        return retry
    return decorator

class GoogleDrive():
    pass
    def __init__(self, oauth_cred=None):
        logger.debug('create GoogleDrive object')
        self.oath_cred = oauth_cred
    
    