#include <stdio.h>

float laskeParkkiMaksu(float tunnit){
    float maksu = 2;
    if (tunnit > 3){
        float yli = tunnit - 3;
        maksu = maksu + yli * 0.5;
    }
    if (maksu > 10.0){
        maksu = 10.0;
    }
    return maksu;
}

int main(void){
    float numbers[3] = {0};
    float maksut[3] = {0};
    float yhtTunnit = 0;
    float yhtMaksut = 0.0;
    printf("%s %s %s\n", "Asiakas", "Tunnit", "Veloitus");
    for(int i=0; i<3; i++){
        scanf("%f", &numbers[i]);
        maksut[i] = laskeParkkiMaksu(numbers[i]);
        yhtTunnit += numbers[i];
        yhtMaksut += maksut[i];
    }
    for (int k=1; k<4; k++){
        printf("%d %0.2f %0.2f\n", k, numbers[k-1], maksut[k-1]);
    }
    printf("%s %0.2f %0.2f\n", "YHTEENSA", yhtTunnit, yhtMaksut);
    return 0;
}
