#include <stdio.h>

int main(){
    double loan, interest = 0;
    int loan_days;
    scanf("%lf", &loan);
    scanf("%lf", &interest);
    scanf("%i", &loan_days);
    interest = interest / 100;
    double interest_value = loan * interest * loan_days/365;
    printf("Lainap‰‰oman %.2f euroa korko %i p‰iv‰lt‰ korkoprosentilla %.2f on yhteens‰ %.2f euroa.", loan, loan_days, interest*100, interest_value);

    return 0;
}
