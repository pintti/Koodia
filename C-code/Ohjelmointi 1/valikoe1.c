#include <stdio.h>

int main(){
    for(int i=6; i>0; --i){
        char stars[7]={};
        for(int k=0; k<i; k++){
            stars[k] = '*';
        }
        printf("%s", stars);
        printf("\n");
    }

    return 0;
}
