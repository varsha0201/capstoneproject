
import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from urllib.request import urlopen
from jose import jwt

#----------------------------------------------------------------------------#
# Auth0 Config
#----------------------------------------------------------------------------#

AUTH0_DOMAIN = 'capstone0201.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Tj0FtObJMX5vs66rqPGkK0BZRlcnFYt1'

#----------------------------------------------------------------------------#
# AuthError Exception
#----------------------------------------------------------------------------#

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
#----------------------------------------------------------------------------#
# Auth Wrapper Methods
#----------------------------------------------------------------------------#

# TODO DONE implement get_token_auth_header() method

def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    *Input: None
    *Output:
       <string> token (part of the header)
    
    Conditions for Output:
       - Authorization header is available
       - header must not be malformed (i.e. Bearer XXXXX)
    """
    if 'Authorization' not in request.headers:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'No Authorization in header.'
            }, 401)
    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')
    if len(header_parts) != 2:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }, 401)
    elif header_parts[0] != 'Bearer':
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }, 401)
    return header_parts[1]



def check_permissions(permission, payload):
    ''' Check if permission is part of payload
    *Input
        <string> permission (i.e. 'post:drink')
        <string> payload (decoded jwt payload)
    *Output:
         True if all conditions have been met '''
    if 'permissions' not in payload:
        raise AuthError({
                'code': 'bad_request',
                'description': 'No permissions in payload.'
            }, 400)
    if permission not in payload['permissions']:
        raise AuthError({
                'code': 'forbidden',
                'description': 'User does not have required permission.'
            }, 403)
    return True

# TODO DONE implement verify_decode_jwt(token) method

def verify_decode_jwt(token):
    # Verify token
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE TOKEN HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload
        # Raise Error if token is not valide anymore.
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)
        # Raise Error if token is claiming wrong audience.
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. '
                               'Please, check the audience and issuer.'
            }, 401)
        # In all other Error cases, give generic error message
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
     # If no payload has been returned yet, raise error.
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 401)

''' Authentification Wrapper to decorate Endpoints with
*Input:
    <string> permission (i.e. 'post:movies')
uses the get_token_auth_header method to get the token
uses the verify_decode_jwt method to decode the jwt
uses the check_permissions method validate claims and check the requested permission
return the decorator which passes the decoded payload to the decorated method
'''

def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # global payload
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(*args, **kwargs)

        return wrapper

    return requires_auth_decorator