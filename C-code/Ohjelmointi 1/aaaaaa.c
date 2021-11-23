#include <stdio.h>

int main(){
    char array[20] = "        ";
    for(int i=7; i>=0; i--){
        array[i] = 'a';
        printf("%s\n", array);
    }
    return 0;
}