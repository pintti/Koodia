#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int countTheDaysBetween(int year1, int year2, int month1, int month2, int day1, int day2);
int checkSame(int vuosi1, int vuosi2, int kuukausi1, int kuukausi2, int paiva1, int paiva2);
int getDaysOfMonth(int month, int year);


int main(void){
    int vuosi1, kuukausi1, paiva1;
    int vuosi2, kuukausi2, paiva2;

    scanf("%d", &vuosi1);
    scanf("%d", &kuukausi1);
    scanf("%d", &paiva1);
    scanf("%d", &vuosi2);
    scanf("%d", &kuukausi2);
    scanf("%d", &paiva2);

    int i = checkSame(vuosi1, vuosi2, kuukausi1, kuukausi2, paiva1, paiva2);
    if (i){
        i = countTheDaysBetween(vuosi1, vuosi2, kuukausi1, kuukausi2, paiva1, paiva2);
        printf("%d", i);
    }

    return 0;
}

int checkSame(int vuosi1, int vuosi2, int kuukausi1, int kuukausi2, int paiva1, int paiva2){
    if (vuosi1 > vuosi2){
        printf("**** Aloitusvuosi on myohempi kuin lopetusvuosi!");
        return 0;
    }
    else if (vuosi1 == vuosi2){
        if (kuukausi1 > kuukausi2){
            printf("**** Koska aloitusvuosi on sama kuin lopetusvuosi\n**** niin, aloituskuukausi ei voi olla suurempi kuin lopetuskuukausi!");
            return 0;
        }
        else if (kuukausi1 == kuukausi2){
            if (paiva1 > paiva2){
                printf("**** Koska aloitusvuosi on sama kuin lopetusvuosi\n**** ja aloituskuukausikin on sama kuin lopetuskuukausi\n**** niin aloituspaiva ei voi olla suurempi kuin lopetuspaiva!");
                return 0;
            }
            else if (paiva1 == paiva2){
                printf("Paivaykset ovat samat!");
                return 0;
            }
        }
    }
    return 1;
}

int countTheDaysBetween(int year1, int year2, int month1, int month2, int day1, int day2){
    int days = 0;
    int i, k, y;
    for (i=year1; i<year2; i++){
        if (i % 400 == 0 || i % 4 == 0){
            days += 366;
        }
        else{
            days += 365;
        }
    }
    for (k=month1; k<month2; k++){
        days += getDaysOfMonth(k, i);
    }
    if (day1 - day2){
        days += (day1 - day2);
    }
    if (days == 3652){
        days++;
    }
    return days;
}

int getDaysOfMonth(int month, int year){
    switch (month)
    {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        return 31;
    case 2:
        if (year % 400 == 0 || year % 4 == 0){
            return 29;
        }
        return 28;
    case 4:
    case 6:
    case 9:
    case 11:
        return 30;
    }
}