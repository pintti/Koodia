#include <stdio.h>
#include <math.h>

int main(){
    int gas, km, i = 0;
    double numbers[100];
    double drive, average = 0;
    while(1){
        //printf("Anna tankatun bensiinin maara ( -1 lopettaa ) > ");
        printf("-1\n");
        scanf("%i", &gas);
        if(gas==-1){
                i--;
            break;
        }
        else{
            //printf("\nAjetut kilometrit > ");
            scanf("%i", &km);
            drive = gas / (float)km;
            //printf("\nKeskikulutus talla tankkauksella on %.3f litraa satasella\n\n", drive);
            printf("%.3f\n", drive*100);
            numbers[i] = drive;
            i++;
        }
    }
    drive = 0;
    for(int k = i; k>=0; --k){
        drive += numbers[k];
    }
    drive /=i+1;
    printf("%.3f", roundf(drive*1000)/10);

    return 0;
}
