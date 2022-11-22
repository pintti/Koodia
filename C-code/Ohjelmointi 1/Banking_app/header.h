#ifndef THIS_IS_MY_HEADER_GUARD
#define THIS_IS_MY_HEADER_GUARD

struct User;
typedef struct User{
    int pinCode;
    int balance;
    char accountNum[23];
    struct User *next;
} User;

void accountNumGet(void);
User *getAccountDetails(char *accountNum);
User *createUser(int pinCode, int balance, char *accountName);
void pinCodeCheck(User *user);
void mainMenu(User *user);
void withdraw(User *user);
void countCashDownSimple(int *cashAmount, int withdrawAmount);
void writeNewFile(User *user);
void deposit(User *user);
void showBalance(User *user);
void clearBuffer(void);

#endif

/* THIS IS THE OLD MAIN FUNCTION
int main(void){
    Main function to start the program. Defines a test User to use for the banking app testing.

    While loop loops through all test users until the one with predefined testAccountNum is matched.
    When match is found, that user is saved as current user.
    char testAccountNum[23] = "FI12 3456 7890 1234 56"; // this is the account number that would be gotten from a bank card.
    createTestUser(); // create test user
    User *temp = head;
    while(temp){
        if (!(strcmp(temp->accountNum, testAccountNum))){
            current = temp; // set current user as the user with matching accountNum
            break;
        }
        temp = temp->next;
    }
    if(current){ //check if user was found at all
        pinCodeCheck();
    }
    return 0;
}
*/

//OLD TEST USER CREATION FUNCTION
/*
void createTestUser(void){
    Creates the test User and allocates it to the head of the User linked list that acts as the banking app database.
    User *test = (User*) malloc(sizeof(User));
    strcpy(test->accountNum, "FI12 3456 7890 1234 56");
    test->balance = 1000; 
    test->pinCode = 1234; 
    test->next = NULL;
    current = test;
    return;
}
*/
