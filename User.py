class User:
    def __init__(self, username, name, img, userLink):
        self.username = username
        self.name = name
        self.img = img
        self.userLink = userLink

    def __str__(self):
        return f"Username: {self.username}, Name: {self.name}, Image: {self.img}, Userlink: {self.userLink}"
    
followers = [
    User("jdoe", "John Doe", "img1.png"),
    User("asmith", "Alice Smith", "img2.png"),
    User("bjones", "Bob Jones", "img3.png")
]

for user in followers:
    print(user)