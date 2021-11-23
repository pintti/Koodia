#include <stdio.h>

int main(){
    int k[10];
    for(int i=0; i<10; i++){
        scanf("%d", &k[i]);
    }
    int big=0;
    for (int i=0; i<10; i++){
        if(big<k[i]){
            big = k[i];
        }
    }
    printf("Suurin syottamasi luku oli %d", big);

    return 0;
}
