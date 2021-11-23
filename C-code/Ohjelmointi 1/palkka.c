#include <stdio.h>

int main(){
    int pay, hours;
    printf("Anna tuntipalkka: ");
    scanf("%i", &pay);
    printf("Tehdyt tunnit: ");
    scanf("%i", &hours);
    printf("Bruttopalkkasi on %i euroa", pay*hours);

    return 0;
}
