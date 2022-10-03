#include <stdio.h>
#include <stdlib.h>

int paivienLukumaaraKuukaudessa(int kk);

int main(void){
    int month = 0;
    scanf("%d", &month);
    int days = paivienLukumaaraKuukaudessa(month);

    if (month != -1){
        printf("Kuukaudessa %d on %d paivaa", month, days);
    }
    else{
        printf("Kuukautta %d ei ole olemassa", month);
    }

    return 0;
}

int paivienLukumaaraKuukaudessa(int kk){
    switch (kk)
    {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        return 31;
    case 2:
        return 28;    
    case 4:
    case 6:
    case 9:
    case 11:
        return 30;
    default:
        return -1;
    }
}
