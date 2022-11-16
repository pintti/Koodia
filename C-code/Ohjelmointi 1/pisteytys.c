#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct contestant{
    char name[20];
    float points;
    struct contestant *next;
};

struct contestant *head = NULL;

void createContestant(void);
void luepois(void);
void removeLetter(char *string, char letter);
void sortContestants(int numOfContestants);
void printContestants(void);

int main(void){
    int numOfContestants = 0;
    scanf("%d", &numOfContestants);
    luepois();
    for (int i=0; i<numOfContestants; i++){
        createContestant();
    }
    sortContestants(numOfContestants);
    printContestants();
    return 0;
}

void createContestant(void){
    struct contestant *cont = (struct contestant*) malloc(sizeof(struct contestant));
    char time[10] = {'\0'};
    float points = 0;
    int min = 0, seconds = 0, microSeconds = 0;
    fgets(cont->name, sizeof(cont->name), stdin);
    for (int i=0; i<4; i++){
        fgets(time, sizeof(time), stdin);
        removeLetter(time, '.');
        sscanf(time, "%d %d %d", &min, &seconds, &microSeconds);
        switch (i)
        {
        case 0:
            points += ((min * 60) + seconds + (0.01 * microSeconds));
            break;
        case 1:
            points += ((min * 60) + seconds + (0.01 * microSeconds))/3;
            break;
        case 2:
            points += ((min * 60) + seconds + (0.01 * microSeconds))/10;
            break;
        case 3:
            points += ((min * 60) + seconds + (0.01 * microSeconds))/20;
            break;
        }
    }
    cont->points = points;
    cont->next = NULL;
    if (head == NULL){
        head = cont;
        return;
    }
    struct contestant *temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = cont;
    return;
}

void luepois(void){
    while( getc(stdin) != '\n');
}

void removeLetter(char *string, char letter){
    for (int i=0; string[i]; i++){
        if (string[i] == letter){
            string[i] = ' ';
        }
    }
}

void sortContestants(int numOfContestans){
    struct contestant *current = head;
    struct contestant *temp;
    char tempName[20] = {'\0'};
    int tempPoints;
    while(current){
        temp = current->next;
        while(temp){
            if (current->points>temp->points){
                current->next = temp->next;
                temp->next = current;
                if (current == head){
                    head = temp;
                }
            }
            temp = temp->next;
        }
        current = current->next;
    }
}

void printContestants(void){
    struct contestant *temp = head;
    int i = 1;
    while(temp){
        printf("%d- %s    %.3f\n", i, temp->name, temp->points);
        temp = temp->next;
        i++;
    }
}
