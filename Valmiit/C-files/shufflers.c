#include <stdio.h>
#include <inttypes.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

uint8_t list[8] = {1, 2, 3, 4, 5, 6, 7, 8};

void shuffle(uint8_t *list, uint16_t list_size);


int main(){
    int i;
    srand(time(NULL));
    shuffle(list, 8);
    for(i=0; i<8; i++){
        printf("%i", list[i]);
    }
    return 0;
}

void shuffle(uint8_t *list, uint16_t list_size){
    uint8_t shufflelist[list_size];
    int i = 0;
    int k = 0;
    for (i = list_size; i > 0; --i) {
        int ran = rand() % i;
        shufflelist[list_size - i] = list[ran];
        for (k = ran; k < list_size; ++k) {
            list[k] = list[k+1];
        }
    }
    for(i=0; i<list_size; ++i){
        list[i] = shufflelist[i];
    }
    return;
}