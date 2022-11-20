#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

User *current = NULL;

int main(void){
    /*Main function.*/
    accountNumGet();
    return 0;
}


void pinCodeCheck(void){
    /*Function that handles the PIN-code check. Using the current user pointer it checks if the
    given PIN-code matches with that saved in the user struct. User is given three tries to input 
    the right code. If all three fail, the program ends and the bank card would be eaten.*/
    int pinCode = 0, tries = 0;
    for(tries = 0; tries<3; tries++){
        printf("Input PIN-code > ");
        scanf("%d", &pinCode);
        if (pinCode == current->pinCode){
            mainMenu();

            return;
        }
        else{
            printf("Wrong code\n%d tries left\n", tries);
        }
    }
    printf("Too many wrong codes given, card will not be returned. Please contact your bank.");
    return;
}


void mainMenu(void){
    /*Main menu function. Works by asking the user for input choice and the proceeding to that function.
    After an operation closes the program.*/
    int option = 0;
    while(1){
        printf("1. Withdraw\n2. Deposit\n3. Show Balance\n0. Exit\n> ");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            withdraw();
            writeNewFile();
            return;
        case 2:
            deposit();
            writeNewFile();
            return;
        case 3:
            showBalance();
            return;
        case 0:
            return;
        default:
        printf("Input not supported");
            break;
        }
    }
}


void createTestUser(void){
    /*Creates the test User and allocates it to the head of the User linked list that acts as the banking app database.*/
    User *test = (User*) malloc(sizeof(User));
    strcpy(test->accountNum, "FI12 3456 7890 1234 56");
    test->balance = 1000; 
    test->pinCode = 1234; 
    test->next = NULL;
    current = test;
    return;
}


void createUser(int pinCode, int balance, char *accountNum){
    /*Function that uses the information gotten from the user and from account file to create 
    the current user that is being handled.
    Arguments:
        int pinCode: users pincode
        int balance: users current balance
        char accountNum: users account information.*/
    User *new = (User*) malloc(sizeof(User));
    strcpy(new->accountNum, accountNum);
    new->pinCode = pinCode;
    new->balance = balance;
    new->next = NULL;
    current = new;
    return;
}


void withdraw(void){
    /*Withdraw function. Asks the user for the amount to withdraw (allows for custom amounts too),
    and then reduces the users accounts balance by that amount.
    The machine can only give 20 and 50 bills so the function check that users input is not an amount 
    that cannot be given with those bills.*/
    int withdrawAmount = 0;
    int moneyAmounts[7] = {20, 40, 60, 80, 100, 150, 200};
    int cashAmount[2] = {0, 0};
    printf("1. 20       2. 40\n3. 60     4. 80\n5. 100      6. 150\n7. 200      8. Other sum\n> ");
    scanf("%d", &withdrawAmount);
    if (withdrawAmount == 8){
        printf("Input amount to withdraw > ");
        scanf("%d", &withdrawAmount);
        if(withdrawAmount % 10 && withdrawAmount != 10 && withdrawAmount != 30){
            printf("Amount needs to be a whole number divisive by 20 and 50!\n");
        }
        else{
            if ((current->balance -= withdrawAmount) < 0){
                printf("Not enough balance.\n");
            }
            else if(withdrawAmount > 1000){
                printf("Cannot withdraw more than 1000.\n");
            }
            else{
                printf("Withdrawing %d.\n", withdrawAmount);
                current->balance -= withdrawAmount;
                countCashDownSimple(cashAmount, withdrawAmount);
                printf("Withdrawn %d 50 euro bills and %d 20 euro bills\n", cashAmount[0], cashAmount[1]);
            }
        }
    }
    else if (withdrawAmount > 0 && withdrawAmount < 8){
        if(current->balance - moneyAmounts[withdrawAmount-1] < 0){
            printf("Not enough balance.\n");
            return;
        }
        else{
            printf("Withdrawing %d.\n", moneyAmounts[withdrawAmount-1]);
            current->balance -= moneyAmounts[withdrawAmount-1];
            countCashDownSimple(cashAmount, moneyAmounts[withdrawAmount-1]);
            printf("Withdrawn %d 50 euro bills and %d 20 euro bills\n", cashAmount[0], cashAmount[1]);
        }
    }
    else{
        printf("Input not supported.\n");
    }
    return;
}


void countCashDownSimple(int *cashAmount, int withdrawAmount){
    /*Count the withdraw amount using a very simple algorithm.
    Arguments:
        int cashAmount: a list containing bills to be given.
        int withdrawAmount: the amount of money being withdrawn.*/
    while(withdrawAmount){
        if(!(withdrawAmount % 50)){
            cashAmount[0]++;
            withdrawAmount -= 50;
        }
        else{
            cashAmount[1]++;
            withdrawAmount -= 20;
        }
    }
    return;
}


void accountNumGet(void){
    /*Function ask the user for account number and then passes that number to another function.*/
    char accountNum[100] = {'\0'};
    int option = 1;
    while(1){
        printf("Give the account number > ");
        fgets(accountNum, sizeof(accountNum), stdin);

        if (accountNum[strlen(accountNum)-1] == '\n'){
            accountNum[strlen(accountNum)-1] = '\0';
        }
        clearBuffer();

        if(getAccountDetails(accountNum)){
            printf("Account found.\n");
            pinCodeCheck();
            return;
        }
        else{
            while(1){
                printf("Account not found.\nTry again?\n1. Yes\n0. No> ");
                scanf("%d", &option);
                if (option == 0){
                    return;
                }
                else if(option == 1){
                    break;
                }
            }
        }
    }
}


void clearBuffer(void)
    /*Function that clears the buffer for future inputs.*/
{
   while (fgetc(stdin) != '\n');
}


int getAccountDetails(char *accountNum){
    /*Function checks the users account details from a file.
    Returns:
        1 if file is found.
        0 if file is not found.*/
    char *accountNumCheck = accountNum;
    FILE *inFile;
    int pinCode, balance;
    strcat(accountNumCheck, ".acc");
    printf("TEST: Opening account %s.\n", accountNum);
    inFile = fopen(accountNumCheck, "r");
    if (inFile != NULL){
        fscanf(inFile, "%d", &pinCode); // might fuck up
        fscanf(inFile, "%d", &balance); // yeah
        printf("TEST: %d, %d\n", pinCode, balance);
        createUser(pinCode, balance, accountNum);
    }
    else{
        return 0;
    }
    return 1;
}


void writeNewFile(void){
    /*Function to write a file containing the new account data.*/
    char fileName[100] = {'\0'};
    FILE *outFile;

    strcpy(fileName, current->accountNum);
    strcat(fileName, ".acc");
    outFile = fopen(fileName, "w");
    if (!(outFile)){
        printf("TEST: Error while writing to file.\n");
        return;
    }
    else{
        fprintf("%d\n", current->pinCode);
        fprintf("%d\n", current->balance);
    }
    return;
}


void deposit(void){
    /*Function for user to add funds to their account.*/
    int depositAmount = 0;
    
    while(1){
        printf("Input the amount to deposit or 0 to exit.\n> ");
        scanf("%d", &depositAmount);

        if (depositAmount > 0){
            current->balance += depositAmount;
            printf("Deposited %d.\n", depositAmount);
            return;
        }
        else if (depositAmount == 0){
            return;
        }
        else{
            printf("Enter a sum larger than zero.\n");
        }
    }
}


void showBalance(void){
    /*Function shows the current balance user has.*/
    printf("Current balance is %d.\n", current->balance);
    return;
}