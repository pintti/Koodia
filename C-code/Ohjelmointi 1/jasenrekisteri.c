#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct jasen
{
    char firstName[20];
    char lastName[20];
    int memberNum;
    int joinDay;
    int payments[5];
    struct jasen *next;
};

void mainMenu(void);
void addNewMember(void);
void deleteMember(void);
void modifyMember(void);
void printMember(void);
void printRegister(void);
void findFromRegister(void);

struct jasen *head = NULL;
struct jasen *last = NULL;

int main(void){
    mainMenu();

    return 0;
}

void mainMenu(void){
    int option = 0;
    while(1){
        printf("\n1 Uuden jasenen lisaaminen\n2 Jasenen tietojen poisto\n3 Jasenen tietojen muuttaminen\n4 Tulosta jasen\n5 Tulosta rekisteri\n6 Haku\n7 Lopetus");
        printf("\n\nValintasi > \n");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            addNewMember();
            break;
        case 2:
            deleteMember();
            break;
        case 3:
            modifyMember();
            break;
        case 4:
            printMember();
            break;
        case 5:
            printRegister();
            break;
        case 6:
            findFromRegister();
            break;
        case 7:
            return;
        }
    }
}


void addNewMember(void){
    char firstName[20], lastName[20];
    int memberNum, joinDay, payments[5], year = 2016;
    printf("\nAnna Jasenen Etu- ja Sukunimi > \n");
    scanf("%s %s", firstName, lastName);
    printf("\nAnna jasennumero > \n");
    scanf("%d", &memberNum);
    printf("\nAnna liittymisvuosi > \n");
    scanf("%d", &joinDay);
    for (int i=0; i<5; i++){
        printf("\nAnna vuoden %d jasenmaksu > \n", i+year);
        scanf("%d", &payments[i]);
    }
    printf("\n");

    struct jasen *member = (struct jasen*) malloc(sizeof(struct jasen));
    strncpy(member->firstName, firstName, strlen(firstName));
    strncpy(member->lastName, lastName, strlen(lastName));
    member->memberNum = memberNum;
    member->joinDay = joinDay;
    member->next = NULL;
    for (int i=0; i<5; i++){
        member->payments[i] = payments[i];
    }
    if (head == NULL){
        head = member;
        return;
    }
    struct jasen *temp = head;
    while (temp->next != NULL){
        temp = temp->next;
    }
    temp->next = member;
    return;
}

void deleteMember(void){
    int delMemberNum = 0;
    printf("Anna poistettavan jasenen jasennumero > ");
    scanf("%d", &delMemberNum);

    struct jasen *current = head;
    struct jasen *prev = NULL;

    if(current == NULL){
        return;
    }

    while(current->memberNum != delMemberNum){
        if (current->next == NULL){
            return;
        }
        else{
            prev = current;
            current = current->next;
        }
    }

    if(current == head){
        head = head->next;
    }
    else{
        prev->next = current->next;
    }

    return;
}

void modifyMember(void){
    int memberNum = 0, option = 0, newMemberNum = 0, newYear = 0, newPay = 0;
    char newFirstName[20], newLastName[20];
    struct jasen *temp = head;
    printf("\nAnna muutettavan jasenen jasennumero > \n");
    scanf("%d", &memberNum);

    while (temp->memberNum != memberNum){
        if (temp->memberNum == memberNum){
            break;
        }
        temp = temp->next;
    }
    if (!(temp)){
        printf("Kayttajaa ei ole olemassa!\n");
        return;
    }

    printf("1 Muuta etunimi\n2 Muuta sukunimi\n3 Muuta jasennumero\n4 Muuta liittymisvuosi\n5 Muuta jasenmaksutietoja\n\nValintasi >\n");
    scanf("%d", &option);

    switch (option)
    {
    case 1:
        printf("Anna uusi etunimi > \n");
        scanf("%s", newFirstName);
        strncpy(temp->firstName, newFirstName, strlen(newFirstName));
        return;
    case 2:
        printf("Anna uusi sukunimi > \n");
        scanf("%s", newLastName);
        strncpy(temp->lastName, newLastName, strlen(newLastName));
        return;
    case 3:
        printf("Anna uusi jasennumero > \n");
        scanf("%d", &newMemberNum);
        temp->memberNum = newMemberNum;
        return;
    case 4:
        printf("Anna uusi liittymisvuosi > \n");
        scanf("%d", &newYear);
        temp->joinDay = newYear;
        return;
    case 5:
        for (int i=0; i<5; i++){
            printf("Anna vuoden %d maksu uudelleen > \n", 2016+i);
            scanf("%d", &newPay);
            temp->payments[i] = newPay;
        }
        return;
    }
    printf("Valinta ei ole hyvaksyttava\n");
    return;
}

void printMember(void){
    int searchNum = 0;
    struct jasen *temp = head;
    printf("\nAnna jasennumero > \n");
    scanf("%d", &searchNum);
    while(temp->memberNum != searchNum){
        temp = temp->next;
    }
    printf("ETUNIMI: %s\n", temp->firstName);
    printf("SUKUNIMI: %s\n", temp->lastName);
    printf("JASENNRO: %d\n", temp->memberNum);
    printf("LIITTVUOSI: %d\n", temp->joinDay);
    printf("\n");
    return;
}

void printRegister(void){
    struct jasen *temp = head;
    printf("\n***************************\n");
    while (temp != NULL){
        printf("ETUNIMI: %s\n", temp->firstName);
        printf("SUKUNIMI: %s\n", temp->lastName);
        printf("JASENNRO: %d\n", temp->memberNum);
        printf("LIITTVUOSI: %d\n\n", temp->joinDay);
        temp = temp->next;
    }
    return;
}

void findFromRegister(void){
    int option = 0;
    char searchName[20];
    int searchNum = 0;
    printf("\n1 Haku etunimella\n2 Haku sukunimella\n3 Haku jasennumerolla\n4 Haku liittymisvuodella\n5 Haku jasenmaksurastien perusteella\n\nValintasi > ");
    scanf("%d", &option);
    struct jasen *temp = head;

    switch (option)
    {
    case 1:
        printf("Anna etunimi > \n");
        scanf("%s", searchName);
        
        while(temp->firstName != searchName){
            temp = temp->next;
        }
        break;
    case 2:
        printf("Anna sukunimi > \n");
        scanf("%s", searchName);
        while(temp->lastName != searchName){
            temp = temp->next;
        }
        break;
    case 3:
        printf("Anna jasennumero > \n");
        scanf("%d", &searchNum);
        while(temp->memberNum != searchNum){
            temp = temp->next;
        }
        break;
    case 4:
        printf("Anna liittymisvuosi > \n");
        scanf("%d", &searchNum);
        while(temp->joinDay != searchNum){
            temp = temp->next;
        }
        break;
    case 5:
        printf("Haetaan maksurastien perusteella > \n");
        while(temp != NULL){
            for (int i=0; i<5; i++){
                if(temp->payments[i] == 0){
                    break;
                }
            }
        }
    }
    printf("ETUNIMI: %s\n", temp->firstName);
    printf("SUKUNIMI: %s\n", temp->lastName);
    printf("JASENNRO: %d\n", temp->memberNum);
    printf("LIITTVUOSI: %d\n", temp->joinDay);
    return;
}
