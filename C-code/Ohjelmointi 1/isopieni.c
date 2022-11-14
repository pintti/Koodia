#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){
    char string[100], upper_string[100], lower_string[100];
    int i = 0;
    fgets(string, 100, stdin);
    while (string[i]){
        upper_string[i] = toupper(string[i]);
        lower_string[i] = tolower(string[i]);
        i++;
    }
    printf("%s %s", lower_string, upper_string);
    return 0;
}