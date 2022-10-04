def check_username(username, valid_domains):#username, valid_domains are parameters
    '''checks if username is valid or not
    print Valid if username is valid, print invalid otherwise
    Return True if username is valid, False otherwise
    '''
    is_valid = False
    if username.count('@') == 1:
        record = username.split('@') # split method returns a list object
        domain = record[1]
        if domain in valid_domains:
            is_valid = True
            print('Username is valid!')        
    if not is_valid:
        print('Username is not valid !!!!')    
    return is_valid # "THROWS" True or False

def check_passwords_match(pass1, pass2): # pass1 and pass2 are parameter
    '''checks if passwords match or not
    print Passwords do not match if passwords do not match
    Returns True is passwords match, False otherwise
    '''    
    match = False
    if pass1 == pass2:
        match = True
    if not match:
        print('Passwords do not match')
    return match    # "Throw" True or False

def check_length(password, length):
    '''
    checks if password has required length or not
    prints Error message if requirement is not met
    Returns True if requrement is met, False otherwise
    '''
    has_length = False
    if len(password) >= length:
        has_length = True
    if not has_length:
        print('Password is less than 8 characters')
    return has_length # "Throws" True or False
        
def check_digit(password):
    '''
    checks if password contains a digit or not
    prints Error message if requirement is not met
    Returns True if requrement is met, False otherwise
    '''    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print('Password is missing a digit')
    return has_digit # "THROW" True or False

def check_capital(password):
    '''
    checks if password contains a capital letter or not
    prints Error message if requirement is not met
    Returns True if requrement is met, False otherwise
    '''     
    has_capital = False
    for char in password:
        if char.isupper():
            has_capital = True
            break
    if not has_capital:
        print('Password is misssing capital letter.')
    return has_capital # "THROWS" True or False

def check_special(password):
    '''
    checks if password contains a special character or not
    prints Error message if requirement is not met
    Returns True if requrement is met, False otherwise
    '''    
    has_special = False
    for char in password:
        if not char.isalnum():
            has_special = True
            break
    if not has_special:
        print('Password is missing a special character')
    return has_special # "THROWS" True or False
        
def main():
    username = input('Enter user name >')
    valid_domains = ('gmail.com','ualberta.ca')
    length = 8
    # valid_username is bound to the object that is_valid is bound to
    valid_username = check_username(username, valid_domains) # "CATCH"
    # check password -- Version 2
    if valid_username:
        password = input('Enter password >')
        c_password = input('Enter password again >')
        confirmed = check_passwords_match(password, c_password) # password, c_password are argument
        if confirmed:
            check_length(password, length)
            check_digit(password)
            check_capital(password)
            check_special(password)
main()