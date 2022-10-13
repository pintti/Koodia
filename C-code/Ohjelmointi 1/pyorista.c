#include <stdio.h>
#include <math.h>

void pyoristaKokonaisluvuksi(float luku);
void pyoristaKymmenesosat(float luku);
void pyoristaSadasosat(float luku);
void pyoristaTuhannesosat(float luku);


void pyoristaKokonaisluvuksi(float luku){
    float rounded = 0.0;
    rounded = floor(luku + 0.5);
    printf("%f %.0f\n", luku, rounded);
}

void pyoristaKymmenesosat(float luku){
    float rounded = 0.0;
    luku = floor(luku * 10 + 0.5) / 10;
    printf("%f %.1f\n", luku, rounded);
}

void pyoristaSadasosat(float luku){
    float rounded = 0.0;
    luku = floor(luku * 100 + 0.5) / 100;
    printf("%f %.2f\n", luku, rounded);
}

void pyoristaTuhannesosat(float luku){
    float rounded = 0.0;
    luku = floor(luku * 1000 + 0.5) / 1000;
    printf("%f %.3f\n", luku, rounded);
}

int main(void){
    float luku = 0;
    for (int i=0; i<5; i++){
        scanf("%f", &luku);
        pyoristaKokonaisluvuksi(luku);
        pyoristaKymmenesosat(luku);
        pyoristaSadasosat(luku);
        pyoristaTuhannesosat(luku);
    }
    return 0;
}