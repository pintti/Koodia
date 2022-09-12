#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int checkNum(int playerNum, int multi1, int multi2);

int main(void){
    srand(time(NULL));
    int playerNum = 0, ranNum1 = 0, ranNum2 = 0, addFlag = 1;
    printf("Anna luku -1 lopettaaksesi\n");
    ranNum1 = rand()%9;
    ranNum2 = rand()%9;
    addFlag = rand()%2;
    if (addFlag){
        printf("Paljonko on luku %d kertaa %d? ", ranNum1, ranNum2);
    }
    else{
        while(ranNum1%ranNum2){
            ranNum1 = rand()%9;
            ranNum2 = rand()%9;
        }
        printf("Paljonko on luku %d jaettuna %d? ", ranNum1, ranNum2);
    }
    while(playerNum != -1){
        scanf("%d", &playerNum);
        if (checkNum(playerNum, ranNum1, ranNum2)){
            printf("Oikein!");
        }
        else if (playerNum != -1){
            printf("Väärin, yritä uudelleen> ");
            playerNum = 0;
        }
    }
    return 0;
}

int checkNum(int playerNum, int multi1, int multi2){
    if (playerNum == multi1*multi2){
        return 1;
    }
    return 0;
}
