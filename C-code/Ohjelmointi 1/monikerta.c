#include <stdio.h>

int main(){
    int num1, num2;
    scanf("%i", &num1);
    scanf("%i", &num2);
    if(num1%num2==0){
        printf("Luku %i on luvun %i monikerta.", num1, num2);
    }
    else{
        printf("Luku %i ei ole luvun %i monikerta.", num1, num2);
    }

    return 0;
}
