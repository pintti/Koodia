typedef struct User User;
struct User{
    int pinCode;
    float balance;
    char accountNum[23];
    User *next;
};

void pinCodeCheck(void);
void createTestUser(void);
void mainMenu(void);
void withdraw(void);
void deposit(void);
void showBalance(void);
void countCashDownSimple(int *cashAmount, int withdrawAmount);