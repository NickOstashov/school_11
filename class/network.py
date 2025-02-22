import uuid


class User:
    def __init__(self, name : str, password : str):
        self.user_name : str = name
        self.password : str = password
        self.friend_list : list = list()
        self.uuid : str = str(uuid.uuid4())

    def print_info(self):
        print(f"user_name : {self.user_name}")
        print(f"password : {self.password}")
        print(f"friend_list : {self.friend_list}")
        print(f"uuid : {self.uuid}")

    def add_friend(self, other : "User"):
        self.friend_list.append(other)
        other.friend_list.append(self)

    def _print_friend(self) -> int:
        print("Ваш список друзей")
        for i in range(0, len(self.friend_list)):
            print(f"{i+1}. {self.friend_list[i]}")

        friend_number = input("Выберите друга для удаления / иначе 0 : ")
        if friend_number == '0':
            return -1

        return int(friend_number)

    def remove_friend(self):
        return self._print_friend()

    def __len__(self):
        return len(self.friend_list)

    def __repr__(self):
        return f"user: {self.user_name} uuid: {self.uuid}"


def main():
    user_1 = User("Иван", "123")

    user_2 = User("Петя", "321")
    user_1.add_friend(user_2)

    user_1.remove_friend()



if __name__ == "__main__":
    main()