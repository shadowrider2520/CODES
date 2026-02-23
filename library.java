package lab;
import java.util.Scanner;
class Book {
	String title;
	String author;
	boolean isBorrowed;
	Book(String title,String author) {
		this.title = title;
		this.author = author;
		this.isBorrowed = false;
	}
	void borrow() {
		if (isBorrowed) {
			isBorrowed = true;
			System.out.println(title + " borrowed successfully");
		}
		else {
			System.out.println(title + " is already borrowed");
		}
	}
	void returnbook() {
		if (isBorrowed) {
			isBorrowed = false;
			System.out.println(title + " returned successfully");
		}
		else {
			System.out.println(title + " is already returned");
		}
	}
	void display() {
		System.out.println("title: " + title + "author: " + author);
	}
}
public class Main { 
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("enter the number of books:");
		int n = sc.nextInt();
		sc.nextLine();
		Book[] books = new Book[n];
		for (int i = 0;i<n;i++) {
			System.out.println("enter the title of the book:");
			String name = sc.nextLine();
			System.out.println("enter the author of the book:");
			String author = sc.nextLine();
			books[i] = new Book(name,author);
		}
		int choice;
		do {
			System.out.println("====Library====");
			System.out.println("1. view books");
			System.out.println("2. borrow book");
			System.out.println("3. return book");
			System.out.println("Search book by title:");
			System.out.println("5. exit");
			System.out.println("Enter your choice:");
			choice = sc.nextInt();
			switch (choice) {
			case 1:
				for (Book b:books) {
					b.display();
					break;
				}
			case 2:
				System.out.println("Enter book title to borrow:");
				String btitle = sc.nextLine();
				boolean foundborrow = false;
				for (Book b:books) {
					if (b.title.equalsIgnoreCase(btitle)) {
						b.borrow();
						foundborrow = true;
						break;
					}
				}
				if (!foundborrow) {
					System.out.println("book not found:");
				}
			case 3:
                System.out.print("Enter book title to return: ");
                String rTitle = sc.nextLine();
                boolean foundReturn = false;
                for (Book b : books) {
                    if (b.title.equalsIgnoreCase(rTitle)) {
                        b.returnbook();
                        foundReturn = true;
                        break;
                    }
                }
                if (!foundReturn) System.out.println("Book not found.");
                break;
			case 4:
				System.out.println("enter book title to search:");
				String stitle =  sc.nextLine();
				boolean foundsearch = false;
				for (Book b:books) {
					if (b.title.equalsIgnoreCase(stitle)) {
						b.display();
						foundsearch = true;
						break;
					}
				}
				if (!foundsearch) {
					System.out.println("book not found");
				}
			case 5:
				System.out.println("exiting....thank you visit us again :)");
			}
			
		}
		while (choice!=5);
	}
}