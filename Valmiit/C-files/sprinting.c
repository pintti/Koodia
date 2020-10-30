#include <stdio.h>
#include <inttypes.h>
#include <math.h>
#include <stdlib.h>

void kirjoita_sensorit(char *str, float ax, float ay, float az, float press, float temp);

int main(){
    char str[100];
    kirjoita_sensorit(str, 0.2536, -5.3272, -1.3277776, 101325.273261, 27.721667);
    printf("%s", str);
    return 0;
}

void kirjoita_sensorit(char *str, float ax, float ay, float az, float press, float temp){
    sprintf(str, "%+.2f,%+.2f,%+.2f,%.0f,%.2f", ax, ay, az, press, temp);
}