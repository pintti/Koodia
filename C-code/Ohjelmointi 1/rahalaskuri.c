#include <stdio.h>
#include <stdlib.h>

void get_worker_pay(int *worker_pay, int workers);
void count_pay(int *money_unit, int *worker_pay, int workers, int unit_amount);
int *foo(int workers);
void print_pays(int *money_unit, int unit_amount);

int main(void){
    int workers = 5, unit_amount = 9;
    int money_unit[9] = {1, 2, 5, 10, 20, 50, 100, 200, 500};
    int worker_pay[5];

    get_worker_pay(worker_pay, workers);
    print_pays(money_unit, unit_amount);
    count_pay(money_unit, worker_pay, workers, unit_amount);

    return 0;
}


void get_worker_pay(int *worker_pay, int workers){
    for (int i=0; i<workers; i++){
        printf("Anna %d. tyontekijan palkka > ", i+1);
        scanf("%d", &worker_pay[i]);
    }
}


void count_pay(int *money_unit, int *worker_pay, int workers, int unit_amount){
    int worker_pay_amount_sum[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    int amount = unit_amount - 1;
    for (int i=0; i<workers; i++){
        int worker_pay_amount[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        int worker_pay_sum = worker_pay[i];
        for (int k=unit_amount; k>=0; k--){
            while (worker_pay_sum >= money_unit[k]){
                worker_pay_sum = worker_pay_sum - money_unit[k];
                worker_pay_amount[amount-k] += 1;
                worker_pay_amount_sum[amount-k] += 1;
            }
        }
        for (int z=-1; z<unit_amount; z++){
            if (z < 0){
                printf("%5d", worker_pay[i]);
            }
            else {
                printf("%5d", worker_pay_amount[z]);
            }
        }
        printf("\n");
    }
    for (int z=-1; z<unit_amount; z++){
            if (z < 0){
                printf(" YHT:");
            }
            else {
                printf("%5d", worker_pay_amount_sum[z]);
            }
    }
    printf("\n");
}


int *foo(int workers){
    int *worker_pay = malloc(workers);
    for (int i=0; i<workers; i++){
        worker_pay[i] = 0;
    }
    return worker_pay;
}


void print_pays(int *money_unit, int unit_amount){
    printf("\n");
    for (int i=-1; i<unit_amount; i++){
        if (i == -1){
            printf("Palkka ");
        }
        else{
            printf("  %d€", money_unit[unit_amount - i - 1]);
        }
    }
    printf("\n");
}