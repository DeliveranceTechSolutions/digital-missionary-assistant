def logout(auth):
    auth.authenticated = False
    auth.loggedin = False
    return auth