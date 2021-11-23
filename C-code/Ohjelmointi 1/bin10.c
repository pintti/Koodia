#include <stdio.h>

int power(int a, int b){
    if(b == 0){
        return 1;
    }
    int num = a;
    b--;
    for(int k=0; k<b; k++){
        num *= a;
    }
    return num;
}

int main(){
    char bin[20];
    int sum = 0;
    scanf("%s", bin);
    char *ptr = bin; 
    for(int i=0; i<=4; i++){
        char c = ptr[i];
        int k = c - '0';
        sum += k*(power(2,4-i));
    }
    printf("%d", sum);
    return 0;
}