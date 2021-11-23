#include <stdio.h>
#include <string.h>

void palindrome(char* string){
    for(int i=0; i<2; i++){
        if(string[i] != string[4-i]){
            printf("Luku %s ei ole palindromi", string);
            return;
        }
    }
    printf("Luku %s on palindromi", string);
}


int main(){
    int input;
    char string[6];
    scanf("%d", &input);
    if (input < 10000 || input >= 100000){
        printf("Syote ei ole viisinumeroinen positiivinen kokonaisluku\n");
    }
    else{
        sprintf(string, "%d", input);
        palindrome(string);
    }
    return 0;
}