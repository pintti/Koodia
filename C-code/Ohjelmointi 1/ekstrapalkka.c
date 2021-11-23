#include <stdio.h>
#include <math.h>

int main(){
    double pay, hours, taxp, brutto, netto, extra_hours, extra_pay = 0;
    scanf("%lf", &pay);
    scanf("%lf", &hours);
    scanf("%lf", &taxp);
    if (hours > 40){
        extra_hours = hours - 40;
        extra_pay = extra_hours * pay * 1.5;
        hours -= extra_hours;
    }
    double pay_out = (pay * hours) + extra_pay;
    float tax = (taxp/(float)100) * pay_out ;
    printf("Nettopalkkasi on %.2lf euroa josta veron osuus on %.2lf euroa", pay_out-tax, roundf(tax*100)/100);
    return 0;
}
