class Book:
    def __init__(self, title, author, publication_date, year):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.year = year

    def display_info(self):
        print(f"Title {self.title}")
        print(f"author {self.author}")
        print(f"publication_date {self.publication_date}")
        print(f"Year {self.year}")

book1 = Book("Oliver_Twist", "Timothy", 23, 2020)


book1.display_info()
