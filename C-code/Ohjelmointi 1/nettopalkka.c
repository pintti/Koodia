#include <stdio.h>
#include <math.h>

int main(){
    double pay, hours, taxp;
    scanf("%lf", &hours);
    scanf("%lf", &pay);
    scanf("%lf", &taxp);
    double tax = (taxp/100)*pay*hours;
    printf("Nettopalkkasi on %.2lf euroa josta veron osuus on %.2lf euroa", pay*hours-tax, roundf(tax*100)/100);

    return 0;
}
