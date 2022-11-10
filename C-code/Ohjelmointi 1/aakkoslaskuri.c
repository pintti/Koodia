#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int countLetterPlace(char letter);

int main(void){
    char string1[100];
    int letters[26], num = 0;
    char letterss[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    for (int i = 0; i<25; i++){
        letters[i] = 0;
    }

    for (int i = 0; i<3; i++){
        scanf("%s", string1);
        int k = 0;
        while (string1[k]){
            num = countLetterPlace(string1[k]);
            if (num){
                letters[num - 1]++;
            }
            k++;
        }
    }
    printf("Aakkonen    Kpl\n");
    for (int i = 0; i<26; i++){
        printf("%c      %d\n", letterss[i], letters[i]);
    }

    return 0;
}


int countLetterPlace(char letter){
    char letters[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    for (int i = 0; i<26; i++){
        if (letters[i] == letter){
            return i+1;
        } 
    }
}
