#include <stdio.h>
#include <math.h>

double laskeHypotenuusa(double, double);

double laskeHypotenuusa(double sivu1, double sivu2){
    return sqrt((sivu1*sivu1 + pow(sivu2, 2)));
}

int main() {
    
    double sivu1 = 0.0;
    double sivu2 = 0.0;
    double hypotenuusa = 0.0;
    
    printf("\nAnna ensimmäinen sivu: ");
    scanf("%lf", &sivu1);
    
    printf("\nAnna toinen sivu: ");
    scanf("%lf", &sivu2);

    hypotenuusa = laskeHypotenuusa(sivu1, sivu2);
    printf("\nHypotenuusa: %f", hypotenuusa);
    
    return 0;
}
