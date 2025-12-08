from faker import Faker

faker = Faker('ru_RU')



def generate_registration_data():
    name = faker.first_name()
    family = faker.last_name()
    address = 'ул. Безымянная д.3'
    phone = faker.numerify('79#########')
    date = faker.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d.%m.%Y")
    text = faker.text(max_nb_chars=30)

    return name, family, address, phone, date, text
