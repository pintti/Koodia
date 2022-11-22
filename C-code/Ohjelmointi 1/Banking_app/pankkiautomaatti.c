#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"


int main(void){
    /*Main function.*/
    accountNumGet();
    return 0;
}


void accountNumGet(void){
    /*Function ask the user for account number and then passes that number to another function.*/
    char accountNum[100] = {'\0'};
    int option = 1;
    User *user;
    while(1){
        printf("Give the account number > ");
        fgets(accountNum, sizeof(accountNum), stdin);

        if (strlen(accountNum)<30){
            if (accountNum[strlen(accountNum)-1] == '\n'){
                accountNum[strlen(accountNum)-1] = '\0';
            }
            
            user = getAccountDetails(accountNum);
            if(user->pinCode){
                pinCodeCheck(user);
                return;
            }
            else{
                while(1){
                    printf("Account not found.\nTry again?\n1. Yes\n0. No > ");
                    scanf("%d", &option);
                    clearBuffer();
                    if (option == 0){
                        return;
                    }
                    else if(option == 1){
                        break;
                    }
                }
            }
        }
        else{
            clearBuffer();
        }
    }
}


User *getAccountDetails(char *accountNum){
    /*Function checks the users account details from a file.
    Returns:
        1 if file is found.
        0 if file is not found.*/
    char *accountNumCheck = accountNum;
    FILE *inFile;
    User *user;
    int pinCode = 0, balance = 0;
    strcat(accountNumCheck, ".acc");
    inFile = fopen(accountNumCheck, "r");
    if (inFile != NULL){
        fscanf(inFile, "%d", &pinCode);
        fscanf(inFile, "%d", &balance);
        printf("TEST: %d, %d", pinCode, balance);
        if (pinCode > 0 && balance >= 0){
            user = createUser(pinCode, balance, accountNum);
            return user;
        }
        return;
    }
    else{
        return;
    }
}


User *createUser(int pinCode, int balance, char *accountName){
    /*Function that uses the information gotten from the user and from account file to create 
    the current user that is being handled.
    Arguments:
        int pinCode: users pincode
        int balance: users current balance
        char accountNum: users account information.*/
    User *new = (User*) malloc(sizeof(User));
    strcpy(new->accountNum, accountName);
    new->pinCode = pinCode;
    new->balance = balance;
    new->next = NULL;
    return new;
}


void pinCodeCheck(User *user){
    /*Function that handles the PIN-code check. Using the current user pointer it checks if the
    given PIN-code matches with that saved in the user struct. User is given three tries to input 
    the right code. If all three fail, the program ends and the bank card would be eaten.*/
    int pinCode = 0, tries = 0, antiTries = 3;
    for(tries = 0; tries<antiTries; tries++){
        printf("Input PIN-code > ");
        scanf("%d", &pinCode);
        clearBuffer();
        if (pinCode == user->pinCode){
            mainMenu(user);

            return;
        }
        else{
            printf("Wrong code\n%d tries left\n", antiTries-tries-1);
        }
    }
    printf("Too many wrong codes given, card will not be returned. Please contact your bank.");
    return;
}


void mainMenu(User *user){
    /*Main menu function. Works by asking the user for input choice and the proceeding to that function.
    After an operation closes the program.*/
    int option = -1;
    while(1){
        printf("1. Withdraw\n2. Deposit\n3. Show balance\n0. Exit\n> ");
        scanf("%d", &option);
        clearBuffer();
        switch (option)
        {
        case 1:
            withdraw(user);
            writeNewFile(user);
            return;
        case 2:
            deposit(user);
            writeNewFile(user);
            return;
        case 3:
            showBalance(user);
            return;
        case 0:
            return;
        default:
            printf("Input not supported\n");
        }
    }
}


void withdraw(User *user){
    /*Withdraw function. Asks the user for the amount to withdraw (allows for custom amounts too),
    and then reduces the users accounts balance by that amount.
    The machine can only give 20 and 50 bills so the function check that users input is not an amount 
    that cannot be given with those bills.
    cashAmount array are pointers to 20 euro bills and 50 euro bills respectively*/
    int withdrawAmount = 0;
    int moneyAmounts[7] = {20, 40, 60, 80, 100, 150, 200};
    int cashAmount[2] = {0, 0};
    while(1){
        printf("1. 20       2. 40\n3. 60       4. 80\n5. 100      6. 150\n7. 200      8. Other sum\n0. Exit\n> ");
        scanf("%d", &withdrawAmount);
        clearBuffer();

        if (withdrawAmount == 8){
            printf("Input amount to withdraw > ");
            scanf("%d", &withdrawAmount);
            clearBuffer();

            if(withdrawAmount % 10 || withdrawAmount == 10 || withdrawAmount == 30){
                printf("Amount needs to be a whole positive number divisive by 20 and 50!\n");
            }
            else if(withdrawAmount < 0){
                printf("Amount needs to be a whole positive number divisive by 20 and 50!\n");
            }
            else if(withdrawAmount == 0){
                return;
            }
            else{
                if ((user->balance -= withdrawAmount) < 0){
                    printf("Not enough balance.\n");
                }
                else if(withdrawAmount > 1000){
                    printf("Cannot withdraw more than 1000.\n");
                }
                else{
                    printf("Withdrawing %d.\n", withdrawAmount);
                    user->balance -= withdrawAmount;
                    countCashDownSimple(cashAmount, withdrawAmount);
                    printf("Withdrawn %d 50 euro bills and %d 20 euro bills\n", cashAmount[0], cashAmount[1]);
                    return;
                }
            }
        }

        else if (withdrawAmount > 0 && withdrawAmount < 8){

            if(user->balance - moneyAmounts[withdrawAmount-1] < 0){
                printf("Not enough balance.\n");
                return;
            }
            else{
                printf("Withdrawing %d.\n", moneyAmounts[withdrawAmount-1]);
                user->balance -= moneyAmounts[withdrawAmount-1];
                countCashDownSimple(cashAmount, moneyAmounts[withdrawAmount-1]);
                printf("Withdrawn %d 50 euro bills and %d 20 euro bills\n", cashAmount[0], cashAmount[1]);
                return;
            }
        }
        else if (withdrawAmount == 0){
            return;
        }
        else{
            printf("Input not supported.\n");
        }
    }
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


void writeNewFile(User *user){
    /*Function to write a file containing the new account data.*/
    char fileName[100] = {'\0'};
    FILE *outFile;

    strcpy(fileName, user->accountNum);
    outFile = fopen(fileName, "w");
    if (!(outFile)){
        return;
    }
    else{
        fprintf(outFile, "%d\n%d\n", user->pinCode, user->balance);
        fclose(outFile);
    }
    return;
}


void deposit(User *user){
    /*Function for user to add funds to their account.*/
    int depositAmount = 0;
    
    while(1){
        printf("Input the amount to deposit or 0 to exit.\n> ");
        scanf("%d", &depositAmount);
        clearBuffer();
        if (depositAmount > 0){
            if (depositAmount % 10 == 0){
                user->balance += depositAmount;
                printf("Deposited %d.\n", depositAmount);
                return;
            }
            else{
                printf("Deposit need to be a whole number consisting of deposit bills (10, 20, 50, 100, 200, 500)\n");
            }
        }
        else if (depositAmount == 0){
            return;
        }
        else{
            printf("Enter a sum larger than zero.\n");
        }
    }
}


void showBalance(User *user){
    /*Function shows the current balance user has.*/
    printf("Current balance is %d.\n", user->balance);
    return;
}


void clearBuffer(void)
    /*Function that clears the buffer for future inputs.*/
{
   while (fgetc(stdin) != '\n');
}
