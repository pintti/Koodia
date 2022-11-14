#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct Node
{
    int number;
    int row_num;
    struct Node* next;
};


void get_lotto_row(int row_num);
void create_lotto_point(int lotto_row_num, int lotto_number, struct Node** head_ref);
void print_lotto_rows(void);
void get_lotto_win_nums(int *lotto_win_row);
void check_lotto_nums(int *lotto_win_row);

struct Node *head = NULL;

int main(void){
    srand(time(NULL));
    int rivit = 0;
    int lotto_winner_nums[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    printf("Montako rivia haluat syottaa (max 5 rivia ) > ");
    scanf("%d", &rivit);

    for (int i = 1; i <= rivit; i++){
        get_lotto_row(i);
    }

    print_lotto_rows();

    get_lotto_win_nums(lotto_winner_nums);

    check_lotto_nums(lotto_winner_nums);
    return 0;
}


void get_lotto_row(int row_num){
    int lotto_number = 0;
    for (int i = 1; i < 8; i++){
        printf("Anna %d rivin %d. numero > ", row_num, i);
        scanf("%d", &lotto_number);
        create_lotto_point(row_num, lotto_number, &head);
    }
}


void create_lotto_point(int lotto_row_num, int lotto_number, struct Node** head_ref){
    struct Node *link = (struct Node*) malloc(sizeof(struct Node));
    struct Node* last = *head_ref;
    link->number = lotto_number;
    link->row_num = lotto_row_num;
    link->next = NULL;

    if (*head_ref == NULL){
        *head_ref = link;
        return;
    }

    while (last->next != NULL) last = last->next;
    last->next = link;
    return;
}


void print_lotto_rows(void){
    struct Node *ptr = head;
    int last_row_num = 0;
    printf("Lottorivit:\n 1  2  3  4  5  6  7\n");
    while(ptr != NULL){
        if (ptr->row_num != last_row_num){
            printf("\n");
            last_row_num = ptr->row_num;
        }
        printf(" %d", ptr->number);
        ptr = ptr->next;
    }
    printf("\n\n");
}


void get_lotto_win_nums(int *lotto_win_row){
    int ranNum, z=0;
    while (lotto_win_row[9] == 0){
        ranNum = rand() % 20;
        for (int k = 0; k <= z; k++){
            if (lotto_win_row[k] == ranNum){
                ranNum = -1;
            }
        }
        if (ranNum != -1){
            lotto_win_row[z] = ranNum;
            z++;
        }
    }
    printf("Oikea rivi: ");
    for (int i = 0; i<10; i++){
        if (i == 7){
            printf("  lisanumerot: ");
        }
        printf(" %d", lotto_win_row[i]);
    }
    printf("\n");
}


void check_lotto_nums(int *lotto_win_row){
    struct Node *ptr = head;
    int row_num = 1, winning_nums = 0, winning_extra_nums = 0;
    while (ptr != NULL){
        if (ptr->row_num != row_num){
            printf("Rivilla %d. on %d oikein ja %d lisanumeroa\n", row_num, winning_nums, winning_extra_nums);
            row_num = ptr->row_num;
            winning_nums = 0, winning_extra_nums = 0;
        }
        for (int i=0; i<10; i++){
            if (ptr->number == lotto_win_row[i]){
                if (i < 7){
                    winning_nums++;
                }
                else{
                    winning_extra_nums++;
                }
            }
        }
        ptr = ptr->next;
    }
    printf("Rivilla %d. on %d oikein ja %d lisanumeroa\n", row_num, winning_nums, winning_extra_nums);
}
