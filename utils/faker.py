from faker import Faker

fake = Faker()

def get_login_faker(num_casos = 5):

    casos = []
    usuariosValidos = "standard_user"
    passwordValido = "secret_sauce"
    for _ in range(num_casos):

        #seteamos casos de exito
        if fake.boolean(chance_of_getting_true=99): #30% de que salga true
            username=usuariosValidos
            password = passwordValido
            login_example=True
        else:
            username = fake.user_name() #aleatorio
            password = fake.password(length=12)
            login_example = False
        
        casos.append((username, password, login_example))

        return casos