from faker import Faker

fake = Faker()

def get_login_faker(num_casos = 5):

    casos = []
    for i in range(num_casos):
        username = fake.user_name()
        password = fake.password(length=12)
        login_example = fake.boolean()