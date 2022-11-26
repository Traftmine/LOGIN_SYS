import random

password_dic = {'password1':'(pWç4iCQ','password2':'FI4.2§=.','lol':'o$B°r1FA'}
username_dic = {'user1':'(pWç4iCQ','user2':'FI4.2§=.','traft':'o$B°r1FA'}

def token():
    choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               #chiffres
               '0','1','2','3','4','5','6','7','8','9',
               #caractères spéciaux
               '@','#','&','é','"','(','§','è','!','ç','à',')','°','-','_','$','*','€','^','¨','£','`','ù','%','=',
               '+',':','/',';','.',',','?','<','>'] #' a été enlevé
    token = ''
    for i in range(8):
        token = token + random.choice(choices)
    return token

def user_login(password : str, username : str):
    password_exist, username_exist = 0, 0
    for clé in password_dic.keys(): #à modifier en utilisant un fichier texte pour stocker, car dans un dico si 2 clés on la même valeur ça bug
        if clé == password:
            password_exist += 1
    for clé in username_dic.keys():
        if clé == username:
            username_exist += 1

    if password_exist == 1 and username_exist == 1:
        if password_dic[password] == username_dic[username]:
            print('Connected')
            return None
        else:
            print('Either your passeword or your username is wrong')
            return None

    elif password_exist > 1:
        for clé in password_dic.keys():
            if password_dic[clé] == username_dic[username]:
                print('Connected /someone has the same/ password')
                return None
    else:
        answer = input("You don't have an account, do you want to make one ? y or n : ")
        if answer == 'yes' or answer == 'y':
            creation_account()
        elif answer == 'no' or answer == 'n':
            print('You chose to not create an account')
            return None
        else:
            print('Wrong answer, you chose to not create an account then')
            return None


def creation_account():
    username, password = input('Your username : '), input('Your password : ')
    password_exist, username_exist = 0, 0
    for clé in username_dic.keys():
        if clé == username:
            username = input("It already exist, you must change your username, your new one is : ")

    user_token = token()

    username_dic[username], password_dic[password] = user_token, user_token
    print('The account have been successfully created')

def main():
    print("1 : se connecter")
    print("2 : créer un compte")
    print("q : créer un compte")
    choix_user = input("Mon choix : ")
    if choix_user == "1":
        username, password = input('Your username : '), input('Your password : ')
        user_login(password, username)
    elif choix_user == "2":
        creation_account()
    elif choix_user == 'q':
        print("I quit")
        return None
    else:
        print('wrong choice')

main()