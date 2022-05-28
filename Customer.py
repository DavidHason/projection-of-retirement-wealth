
class Gender():
    GENDER_MALE = 0
    GENDER_FEMALE = 1


class Customer():
    def __init__(self, id, post, seifa, age, gender, prev_acc, acc_bal,growth):
        self.id = id
        self.post = post        # post code
        self.seifa = seifa
        self.age = age          # age
        self.gender = gender
        self.growth = growth
        self.prev_acc = prev_acc
        self.acc = acc_bal

