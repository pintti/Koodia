#include <stdlib.h>
#include <stdio.h>

int main(){
    for(int i=0; i<=100; i++){
        if(i % 3 == 0 || i % 5 == 0){
            if(i % 3 == 0){printf("Fizz");}
            if(i % 5 == 0){printf("Buzz");}
            printf("\n");}
        else{printf("%i\n", i);}
    }
    return 0;
}