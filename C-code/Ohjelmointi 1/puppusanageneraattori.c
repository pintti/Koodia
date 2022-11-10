#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void){
    srand(time(NULL));
    char subs[5][100] = {{'\0'}, {'\0'}, {'\0'}, {'\0'}, {'\0'}};
    char verbs[5][100] = {{'\0'}, {'\0'}, {'\0'}, {'\0'}, {'\0'}};
    char input[20];
    int numOfStrings = 0, z = 0, y = 0, w = 0, x = 0, ran = 0;

    for (int i=0; i<10; i++){
        if(i % 2){
            printf("Anna verbi (max 100 merkkia) > ");
        }
        else{
            printf("Anna substantiivi (max 100 merkkia) > ");
        }
        fgets(input, sizeof(input), stdin);
        if(i % 2){
            strcpy(subs[z], input);
            z++;
        }
        else{
            strcpy(verbs[y], input);
            y++;
        }
    }
    printf("Montako puppulausetta generoidaan > ");
    scanf("%d\n", &numOfStrings);

    printf("---Puppulauseet---\n");

    for (int i=0; i<numOfStrings; i++){
        z = rand()%5;
        y = rand()%5;
        w = rand()%5;
        x = rand()%5;
        ran = rand()%4;
        switch (ran)
        {
        case 0:
            printf("%s %s.\n", subs[z], verbs[y]);
            break;
        case 1:
            printf("%s %s ja %s %s.\n", subs[z], verbs[y], subs[w], verbs[x]);
            break;
        case 2:
            printf("%s %s tai %s %s.\n", subs[z], verbs[y], subs[w], verbs[x]);
            break;
        case 3:
            printf("Jos %s %s, niin %s %s.\n", subs[z], verbs[y], subs[w], verbs[x]);
            break;
        }

    }

    return 0;
}