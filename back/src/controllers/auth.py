from ..repositories.user import UserRepository
from  .contracts.main_controller import MainController
from  ..utils.security import Security

class AuthController(MainController):

    def __init__(self):
        self.security = Security()
        self.user_repository = UserRepository()

    def login(self, data):

        user = self.user_repository.get_user_to_authenticate(email = data['email'])

        if user is None:
            return self.error('Invalid user')

        if not self.security.validate_password(user.password,data['password']):
            return self.error('Invalid user')

        return self.success(data={'token': self.security.generate_jwt(user)})

    def register(self, data):
        data['password'] = self.security.encryp_password(data['password'])
        row = self.user_repository.create(data)
        return self.success(data=row)


