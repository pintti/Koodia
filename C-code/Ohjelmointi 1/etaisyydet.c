#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
    float points_x[5] = {0.0, 0.0, 0.0, 0.0, 0.0};
    float points_y[5] = {0.0, 0.0, 0.0, 0.0, 0.0};
    float route = 0.0, straight = 0.0;
    for (int i = 0; i<5; i++){
        scanf(" %f", &points_x[i]);
        scanf(" %f", &points_y[i]);
    }

    for (int i = 0; i<4; i++){
        route += sqrt(pow(points_x[i] - points_x[i+1], 2) + pow(points_y[i] - points_y[i+1], 2));
    }

    straight = sqrt(pow(points_x[0] - points_x[4], 2) + pow(points_y[0] - points_y[4], 2));

    printf("Etaisyys mutkitellen on %.3f\n", route);
    printf("Alku ja loppupisteiden valinen etaisyys on %.3f", straight);

    return 0;
}
