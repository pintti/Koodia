#include <stdio.h>

void etsiMerkkijonoAlusta(char * string1, char * string2, char * string3);

int main(void) {
    char mjono1[100];
    char mjono2[100];
    char loydetty[10]={'\0'}; 
    
    scanf("%s\n", mjono1);
    scanf("%s\n", mjono2);

    etsiMerkkijonoAlusta(mjono1, mjono2, loydetty); 
    printf("%s", loydetty);
    
    return 0;
}

void etsiMerkkijonoAlusta(char * string1, char * string2, char * string3){
    int i = 0;
    char *copy1 = string1, *copy2 = string2;
    while(copy1[i] != '\0'){
        if (copy1[i] == copy2[i]){
            string3[i] = copy1[i];
            i++;
        }
        else{
            return;
        }
    }
}