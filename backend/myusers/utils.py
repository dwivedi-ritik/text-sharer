from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


def get_tokens_for_user(user):
    access = AccessToken.for_user(user)
    refresh = RefreshToken.for_user(user)
    access['first_name'] = user.first_name
    access['last_name'] = user.last_name
    access['email'] = user.email
    access['username'] = user.username
    return {
        'refresh': str(refresh),
        'access': str(access),
    }
