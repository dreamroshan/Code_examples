class Account(object):
    def __init__(self,name,acc_no):
        self.name = name;
        self.acc_no = acc_no;

    def display(self):
        print "\nEmployee Details : ";
        print "\nCustomer name : ",name;
        print "\nAccount number :",acc_no;

class Saving_account(Account):
    def __init__(self,name,acc_no,bal):
        super(Saving_account,self).__init__(name,acc_no);
        self.bal =bal;

    def display(self):
        super(Saving_account,self).display();
        print "\nBalance: ",bal;

class Account_details(Saving_account):
    def __init__(self,name,acc_no,bal,deposits,withdrawl):
        super(Account_details,self).__init__(name,acc_no,bal);
        self.deposits = deposits;
        self.withdrawl = withdrawl;
    def display(self):
        super(Account_details,self).display();
        print "\nDeposits: ",deposits ;
        print "\nWithdrawl:",withdrawl;

name=raw_input("\nEnter name:");
acc_no=int(raw_input("Enter account number: "))
bal=int(raw_input("\Enter balance:"));
deposits=int(raw_input("\nEnter deposit amount:"))
withdrawl=int(raw_input("\nEnter withdrawl amount: "))

ad=Account_details(name,acc_no,bal,deposits,withdrawl);
ad.display();
