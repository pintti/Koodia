#include <stdio.h>
#include <stdlib.h>

struct arvosana
{
    int grade;
    int drink_num;
    struct arvosana* next;
};

void ask_grade(void);
void create_grade_point(struct arvosana **head_ref, int grade, int drink_num);
void count_grades(void);

struct arvosana *head = NULL;

int main(void){
    ask_grade();
    count_grades();
    return 0;
}


void ask_grade(void){
    int grade = 0;
    for (int i = 1; i<5; i++){
        printf("Anna juoma numero %d. pisteet \n", i);
        for (int k=0; k<10; k++){
            while (!(grade > 0 && grade < 6)){
                printf("Anna arvosana (1-5) > ");
                scanf("%d", &grade);
                if (!(grade > 0 && grade < 6)){
                    printf("\nARVOSANAN TULE\nOLLA VALILTA 1 - 5 !\n");
                }
            }
            create_grade_point(&head, grade, i);
            grade = 0;
        }
    }
}


void create_grade_point(struct arvosana **head_ref, int grade, int drink_num){
    struct arvosana *next_grade = (struct arvosana*) malloc(sizeof(struct arvosana));
    struct arvosana *last = *head_ref;

    next_grade->grade = grade;
    next_grade->drink_num = drink_num;
    next_grade->next = NULL;

    if (*head_ref == NULL){
        *head_ref = next_grade;
        return;
    }

    while (last->next != NULL){
        last = last->next;
    }
    last->next = next_grade;
    return;
}


void count_grades(void){
    struct arvosana *ptr = head;
    int grade_sum = 0, count = 0, drink_num = 1;
    float avg = 0.0;
    while (ptr != NULL){
        if (ptr->drink_num != drink_num){
            printf("Juoma numero %d on ", drink_num);
            avg = grade_sum / count;
            if (avg > 3.0){
                printf("kelvollista\n");
            }
            else{
                printf("kelvotonta\n");
            }
            avg = 0.0;
            grade_sum = 0, count = 0;
            drink_num = ptr->drink_num;
        }
        grade_sum += ptr->grade;
        count ++;
        ptr = ptr->next;
    }
}