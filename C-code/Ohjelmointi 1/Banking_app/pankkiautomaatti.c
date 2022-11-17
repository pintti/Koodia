#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

User *head = NULL;
User *current = NULL;

int main(void){
    /*Main function to start the program. Defines a test User to use for the banking app testing.

    While loop loops through all test users until the one with predefined testAccountNum is matched.
    When match is found, that user is saved as current user.*/
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


void pinCodeCheck(void){
    /*Function that handles the PIN-code check. Using the current user pointer it checks if the
    given PIN-code matches with that saved in the user struct. User is given three tries to input 
    the right code. If all three fail, the program ends and the bank card would be eaten.*/
    int pinCode = 0, tries = 0;
    for(tries = 0; tries<3; tries++){
        printf("Syota PIN-koodi > ");
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
    /*Main menu function*/
    int option = 0;
    while(1){
        printf("1. Withdraw\n2. Deposit\n3. Show Balance\n0. Exit\n> ");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            withdraw();
            return;
        case 2:
            deposit();
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
    head = test;
    return;
}


void withdraw(void){
    /*Withdraw function*/
    int withdrawAmount = 0;
    int moneyAmounts[7] = {20, 40, 60, 80, 100, 150, 200};
    int cashAmount[2] = {0, 0};
    printf("1. 20       2. 40\n3. 60     4. 80\n5. 100      6. 150\n7. 200      8. Other sum\n> ");
    scanf("%d", &withdrawAmount);
    if (withdrawAmount == 8){
        printf("Input amount to withdraw > ");
        scanf("%d", &withdrawAmount);
        if ((current->balance -= withdrawAmount) < 0){
            printf("Not enough balance.\n");
        }
        else if(withdrawAmount > 1000){
            printf("Cannot withdraw more than 1000.\n")
        }
        else{
            printf("Withdrawing %d.\n", withdrawAmount);
            current->balance -= withdrawAmount;
            countCashDownSimple(cashAmount, withdrawAmount);
            printf("Withdrawn %d 50 euro bills and %d 20 euro bills\n", cashAmount[0], cashAmount[1]);
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
    /*Count the withdraw amount using a very simple algorithm.*/
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
