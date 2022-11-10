#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int omaStrcmp(char * string1, char * string2);

int main(void){
    char string1[20] = {'\0'}, string2[20] = {'\0'};
    scanf(" %s", string1);
    scanf(" %s", string2);
    int ret = omaStrcmp(string1, string2);
    if (ret > 0){
        printf("%s > %s", string1, string2);
    }
    else if (ret < 0){
        printf("%s < %s", string1, string2);
    }
    else{
        printf("%s == %s", string1, string2);
    }
    return 0;
}

int omaStrcmp(char * string1, char * string2){
    int i = 0;
    char * copy1 = string1, *copy2 = string2;
    if (strlen(copy1) == strlen(copy2)){
        while (copy1[i]){
            printf("%c %c\n", copy1[i], copy2[i]);
            if (copy1[i] > copy2[i]){
                return 1;
            }
            else if (copy1[i] < copy2[i]){
                return -1;
            }
            i++;
        }
        return 0;
    }
    else{
        if(strlen(copy1) > strlen(copy2)){
            return 1;
        }
        else{
            return -1;
        }
    }
}