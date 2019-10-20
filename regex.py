import re


def isphoneNumber(num):

    phoneNumRegex = '(\d{3})-(\d{3})-(\d{3})'

    if  (re.search(phoneNumRegex, num)):
        print('Valid phone number')
    else:
        print('Wrong phone number format')


def isemailAddress(email):

    #veriEmail = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2, 3)$')
    #email = veriEmail.search(text)

    veriEmail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(veriEmail, email)):
        print("Valid email address")
    else:
        print("Invalid email address")


def personFind(name):
    get_name = '^C.*?n$'
    name = name.title()
    if(re.search(get_name, name)):
        print('Welcome ' + name)
    else:
        print("name doesn't exist ")


isphoneNumber('Here is my phone number 123-709-989')
isemailAddress('dodo@email.com')
personFind('chr-stian')