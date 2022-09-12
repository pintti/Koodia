#include <stdio.h>
#include <stdlib.h>


int countTime(int hour, int min, int sec){
    return sec + (60*min) + (60*60*hour);
}

int * countBack(int time){
    static int times[3];
    while (time > 3600) {
        time -= 3600;
        times[0]++;
    }
    while (time > 60){
        time -= 60;
        times[1]++;
    }
    times[2] = time;
    return times;
}

int main(void){
    int seconds[2];
    int minutes[2];
    int hours[2];
    for (int i=0; i<2; i++){
        scanf("%i", &hours[i]);
        scanf("%i", &minutes[i]);
        scanf("%i", &seconds[i]);
    }
    int firstAll = countTime(hours[0], minutes[0], seconds[0]);
    int secondAll = countTime(hours[1], minutes[1], seconds[1]);

    int *times = countBack(abs(firstAll-secondAll));

    printf("%i\n", abs(firstAll-secondAll));
    printf("%i %i %i", times[0], times[1], times[2]);
    return 0;
}
