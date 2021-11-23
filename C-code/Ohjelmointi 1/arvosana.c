#include <stdio.h>

int main(){
    int points;
    scanf("%i", &points);
    if(0<=points && points<=11){
        printf("Hylatty");
    }
    else if(points>=12 && points<=13){
        printf("1");
    }
    else if(points>=14 && points<=16){
        printf("2");
    }
    else if(points>=17 && points<=19){
        printf("3");
    }
    else if(points>=20 && points<=22){
        printf("4");
    }
    else if(points>=23 && points<=24){
        printf("5");
    }
    else{
        printf("Virheellinen pistemaara");
    }

    return 0;
}
