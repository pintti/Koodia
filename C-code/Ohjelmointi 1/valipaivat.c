#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    char pvm1[10], pvm2[10];
    char *vali;
    int aika1[3], aika2[3];

    scanf("%s", pvm1);
    scanf("%s", pvm2);

    vali = strtok(pvm1, ".");
    printf("%s", vali);
    vuosi1 = *vali;
    printf("%d", vuosi1);

    return 0;
}
