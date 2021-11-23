#include <stdio.h>

int main(){
    int num = 1;
    int a;
    for(int i = 1; i<=10; i++){
        for(int k=10-i; k>0; k--){
            printf(" ");
        }
        for(a=num; a<num+i; a++){
            if(a==10){
                printf("%d", 0);
            }
            else if(a>10){
                printf("%d", a-10);
            }
            else{
                printf("%d", a);
            }
        }
        a-=2;
        while(a>=num){
            if(a==10){
                printf("%d", 0);
            }
            else if(a>10){
                printf("%d", a-10);
            }
            else{
                printf("%d", a);
            }
            a--;
        }
        printf("\n");
        num++;
    }
}