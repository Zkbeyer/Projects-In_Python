class Book:

    def __init__(self,title,author,year):
        self.__title = title;
        self.__author = author;
        self.__year = year
        self.__status = "available";

    def check_out(self):
        if self.__status == "available":
            self.__status = "checked out";
            return "Checked out";
        else:
            return "Book is not available";

    def return_book(self):
        if self.__status == "checked out":
            self.__status = "available";
            return "Book returned";

        else:
            return "Book is not checked out";

        return;

    def get_info(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nYear: {self.__year}"
