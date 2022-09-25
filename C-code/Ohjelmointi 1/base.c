#include <stdio.h>
#include <stdlib.h>

void biggest(int *table);
void avg(int *table);

int main(void){
    int table[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    int value = 0, i = 0;
    while(table[9] == -1){
        printf("Anna %d. kokonaisluku > ", i+1);
        scanf("%d", &value);
        while (value > 100 || value < 0){
            printf("Ei kelpaa, anna %d. kokonaisluku uudestaan > ", i+1);
            scanf("%d", &value);
        }
        table[i] = value;
        i++;
    }
    printf("Taulukon:\n");
    for (int i = 0; i < 10; i++){
        printf("%d ", table[i]);
    }
    
    biggest(table);
    avg(table);

    return 0;
}

void biggest(int *table){
    int big = 0, index = 0;
    for (int i = 0; i < 10; i++){
        if (table[i] > big){
            big = table[i];
            index = i;
        }
    }
    printf("\nSuurin arvo on %d, ja se sijaitsee paikassa %d\n", big, index);
}

void avg(int *table){
    float aveg = 0;
    for (int i = 0; i < 10; i++){
        aveg += table[i];
    }
    aveg = aveg / 10;
    printf("Taulukon arvojen keskiarvo on %f", aveg);
}
