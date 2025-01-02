from faker import Faker


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.username = self.fake.first_name()
        self.email = self.fake.email()
        self.password = self.fake.password(length=12)
        self.task_name = self.fake.sentence()
        self.task_description = ' '.join(self.fake.sentences(nb=3))
        self.comment = self.fake.sentence()
        self.project_name = ' '.join(self.fake.words(nb=3)).upper()
