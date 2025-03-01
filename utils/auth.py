import os
import jwt
from datetime import datetime as date


def get_token():
    key = os.environ.get('ADMIN_API_KEY')

    id, secret = key.split(':')
    iat = int(date.now().timestamp())

    header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
    payload = {
        'iat': iat,
        'exp': iat + 5 * 60,
        'aud': '/admin/'
    }

    token = jwt.encode(payload, bytes.fromhex(secret),
                       algorithm='HS256', headers=header)
    return token
