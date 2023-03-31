class Student:
    def __init__(self, name, stud_id):
        self.name = name
        self.id = stud_id
        self.laptop = self.Laptop()

    def show(self):
        print(f"name: {self.name}  id: {self.id} \n"
              f"brand: {self.laptop.brand}  cpu: {self.laptop.cpu} ram: {self.laptop.ram}")

    class Laptop:

        def __init__(self, brand='Hp', cpu='i5', ram=8):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram


print("Создаем двух студентов")
s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)
s1.show()
s2.show()


print("Увеличиваем память у ноутбука студента s1")
s1.laptop.ram = 16
s1.show()

print("У каждого студента отдельный ноутбук (уникальный объект)")
lap1 = s1.laptop
lap2 = s2.laptop
print(id(lap1))
print(id(lap2))
