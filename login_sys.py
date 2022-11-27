import random

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
    fichier = open("data.txt", "r")

    password_exist, username_exist = 0, 0
    for clé in fichier.readlines(): #on parcours les lignes du fichier
        for words in clé.split(): #on parcours les mots d'une ligne
            if words == password:
                password_exist += 1

    fichier.close()
    fichier = open('data.txt','r')

    for clé in fichier.readlines():
        for words in clé.split():
            if words == username:
                username_exist += 1

    fichier.close()
    fichier = open('data.txt','r')

    if password_exist == 1 and username_exist == 1:
        fichier = open('data.txt','r')
        for lines in fichier.readlines():
            liste = lines.split()
            if liste[0] == username and liste[1] == password:
                print('Connected')
                fichier.close()
                return None
        print('Either your passeword or your username is wrong')
        fichier.close()
        return None

    elif password_exist > 1:
        fichier = open('data.txt','r')
        similar_pass, token_list, same_token, token_s = [], [], 0, ''
        for lines in fichier.readlines():
            words = lines.split()
            token_list.append(words[2])

            if words[1] == password:
                similar_pass.append(words[2])
            if words[0] == username:
                token_s = words[2]

        for element in similar_pass:
            if element == token_s:
                same_token += 1
        if same_token == 1:
            print("connected")
        else:
            print("weird you don't exist")
        fichier.close()

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
    fichier = open('data.txt','r')

    for lines in fichier.readlines():
        words = lines.split()
        if words[0] == username:
            username = input("It already exist, you must change your username, your new one is : ")

    fichier.close()
    user_token = token()

    fichier = open('data.txt','a')
    fichier.write("\n"+username+" "+password+" "+user_token)
    fichier.close()
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
        print("The exit was a success")
        return None
    else:
        print('wrong choice')

main()