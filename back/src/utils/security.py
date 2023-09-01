from .base import bcrypt
from decouple import config
from datetime import datetime, timedelta
import pytz
import jwt


class Security:
    secret = config('SECRET_KEY')
    secret_jwr = config('JWT_KEY')
    tz = pytz.timezone("America/Mexico_City")

    def encryp_password(self, password: str) -> str:
        return bcrypt.generate_password_hash(password=password, rounds=5).decode('utf-8')

    def validate_password(self, password, candidate):
        return bcrypt.check_password_hash(pw_hash=password, password=candidate)

    def generate_jwt(self, user):
        payload = {
            'iat': datetime.now(tz=self.tz),
            'exp': datetime.now(tz=self.tz) + timedelta(hours=10),
            'user': user.id,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def verify_jwt(self, token):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            if len(token) > 0:
                try:
                    return jwt.decode(token, self.secret, algorithms=["HS256"])
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False


