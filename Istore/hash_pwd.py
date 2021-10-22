import hashlib
import InternetStore.settings

def hash_pwd(heslo):

    hasher=hashlib.sha256()
    hasher.update(heslo+InternetStore.settings.SECRET_KEY)
    return hasher.hexdigest()
