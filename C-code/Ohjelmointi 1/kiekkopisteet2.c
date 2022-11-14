#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char name[30];
    int wins;
    int losses; 
}Team;

Team readTeamStats(void);
void sortOrder(int * order, Team * registeri, int numOfTeams);
void luepois(void);

int main(void){
    Team registeri[3];
    int order[3] = {0, 1, 2};
    int numOfTeams = 0;
    scanf("%d", &numOfTeams);
    for (int i = 0; i<numOfTeams; i++){
        registeri[i] = readTeamStats();
    }
    sortOrder(order, registeri, numOfTeams);

    for (int i = 0; i<numOfTeams; i++){
        printf("%s %d voittoa %d tappiota\n", registeri[order[i]].name, registeri[order[i]].wins, registeri[order[i]].losses);
    }

    return 0;
}

Team readTeamStats(void){
    Team tempTeam;
    luepois();
    printf("\nJoukkue nimi>");
    fgets(tempTeam.name, sizeof(tempTeam.name), stdin);
    printf("Joukkue voitot>");
    scanf("%d", &tempTeam.wins);
    printf("Joukkue tappiot>");
    scanf("%d", &tempTeam.losses);
    return tempTeam;
}

void sortOrder(int * order, Team * registeri, int numOfTeams){
    int tempOrderNum = 0, tempPoints = 0;
    for (int i = 0; i<numOfTeams; i++){
        int OrderNum = i, points = registeri[i].wins - registeri[i].losses;
        if (!(tempPoints)){
            tempOrderNum = i;
            tempPoints = points;
        }
        else{
            if (points > tempPoints){
                order[tempOrderNum] = i;
                order[i] = tempOrderNum;
                tempOrderNum = i; 
            }
        }
    }
}

void luepois(void){
 while( getc(stdin) != '\n');
}
