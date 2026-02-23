import java.util.Scanner;
class Account {
	String accno;
	String name;
	double balance;
	Account(String accno,String name,double balance) {
		this.accno = accno;
		this.name = name;
		this.balance = balance;
	}
	void deposit(double amount) {
		balance+=amount;
		System.out.println("Deposited " + amount + " successfully");		
	}
	void withdraw(double amount) {
		if (amount>0 && amount<balance) {
			balance-=amount;
			System.out.println("withdrawed " + amount + " successfully");
		}
		else {System.out.println("insufficient balance");		}
	}
	void display() {
		System.out.println("Accno: " + accno + "name: " + name + "balance: " + balance);
	}
}
public class Main {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("enter the number of accounts:");
		int n = sc.nextInt();
		Account[] accounts = new Account[n];
		for (int i =0;i<n;i++) {
			System.out.println("enter the account number:");
			String accno = sc.nextLine();
			System.out.println("enter the name:");
			String name = sc.nextLine();
			System.out.println("enter the initial balance:");
			double bal = sc.nextDouble();
			accounts[i] = new Account(accno,name,bal);
		}
		int choice;
		do {
			System.out.println("========Bank of Palkowa=====");
			System.out.println("1.Deposit");
			System.out.println("2. withdraw");
			System.out.println("3. view Accounts");
			System.out.println("4. Exit");
			System.out.println("enter the choice:");
			choice = sc.nextInt();
		
		switch (choice) {
		case 1:
			System.out.println("enter account number:");
			String acc = sc.nextLine();
			System.out.println("Enter amount:");
			double amt = sc.nextDouble();
			for (Account a:accounts) {
				if (a.accno==acc) {
					a.withdraw(amt);
				}
				else {
					System.out.println("Account not found");
				}
			}
			break;
		case 2:
			for (Account a:accounts) {
				System.out.println("enter account number:");
				String wacc = sc.nextLine();
				System.out.println("Enter amount:");
				double wamt = sc.nextDouble();
				for (Account w:accounts) {
					if (w.accno==wacc) {
						a.withdraw(wamt);
					}
					else {
						System.out.println("account not found");
					}
				}
				break;
			}
		case 3:
			for (Account d: accounts) {
				d.display();
			}
			break;
		default:
			System.out.println("invalid choice:");
		}}
		while (choice!=4);
		sc.close();
	}}
	

