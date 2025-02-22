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