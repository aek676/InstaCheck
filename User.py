class User:
    def __init__(self, username, name, img, userLink):
        self.username = username
        self.name = name
        self.img = img
        self.userLink = userLink

    def __str__(self):
        return f"Username: {self.username}, Name: {self.name}, Image: {self.img}, Userlink: {self.userLink}"