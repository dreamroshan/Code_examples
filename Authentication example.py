class Authentication(Exception):
    def display(self):
        print"\nAuthentication Failed..." ;
name = raw_input("\nEnter your name: ");
password = int(raw_input("\nEnter your password: "));

try:
    if(password== 123):
        print"\nAuthenticated User..." ;
    else:
        raise Authentication();
except Authentication,a:
    a.display();