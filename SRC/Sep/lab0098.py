a = 10  # -- #globle variable it able to use in clas


class person:
    b = 11  # instance varible - Belong to class

    def print_infor(self):
        print(a)
        print(self.b)


object_ref = person()
object_ref.print_infor()
print(a)
