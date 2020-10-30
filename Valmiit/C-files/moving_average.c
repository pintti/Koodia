#include <stdio.h>
#include <inttypes.h>
#include <math.h>
#include <stdlib.h>

void movavg(float *array, uint8_t array_size, uint8_t window_size);

int main(){
    float data[5] = { 1.0, 2.0, 4.0, 6.0, 9.0 };
    movavg(data, 5, 3);
    return 0;
}

void movavg(float *array, uint8_t array_size, uint8_t window_size){
    float print_data[array_size];
    int i=0;
    int p=0;
    for(i=0; i<=array_size-window_size; i++){
        float count=0.0;
        for(p=0; p<window_size; p++){
            count = count + array[i+p];
        }
        print_data[i] = count/window_size;
    }
    for(i=0; i<array_size-window_size; i++){
        printf("%.2f,", print_data[i]);
    }
    printf("%.2f", print_data[array_size-window_size]);
}