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
    int option = 0;
    while(1){
        printf("1. Withdraw\n2. Deposit\nShow Balance\n0. Exit\n> ");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            withdraw();
            break;
        case 2:
            deposit();
            break;
        case 3:
            showBalance();
            break;
        case 0:
            return;
        default:
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

}
