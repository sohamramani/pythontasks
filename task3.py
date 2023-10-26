error = [
  ("Username should have at least one '.'", lambda usernamefield:"." in usernamefield),
  ("Username should have at least one '_'", lambda usernamefield:"_" in usernamefield),
  ("Username should be at least 8 characters long", lambda usernamefield: len(usernamefield)>=8),
  ("password must be contain Atleast one of the following '@,#,$,%'", lambda pwdfield: any(value in pwdfield for value in ['@', '#', '$','%'])),
  ("password must be contain Atleast one uppercase letter", lambda pwdfield: any(value.isupper() for value in pwdfield)),
  ("password must be contain Atleast one lowercase letter", lambda pwdfield: any(value.islower() for value in pwdfield)),
  ("Password should have at least one digit from 0-9", lambda pwdfield: any(value.isdigit() for value in pwdfield))
]
usernamefield = input("Enter Your Username : ")
username_errors = [condition for condition, check in error[:3] if not check(usernamefield)]
for  errorstatment in username_errors:
    print(errorstatment)
    username = input("Enter a username: ")
    if len(username_errors) == '0':
        break

pwdfield = input("Enter your password: ")
pass_error = [condition for condition, check in error[3:] if not check(pwdfield)]
for  errorstatment in pass_error:
    print(errorstatment)
    pwdfield = input("Enter your password: ")
    if len(pass_error) == '0':
        break

print("Username is: ", usernamefield)
print("Password is: ", pwdfield)