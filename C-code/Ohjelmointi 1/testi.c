#include <stdio.h>     /* printf ja scanf */
/* #define KM_MAILISSA 1.609 muunnosvakio makron avulla */
const double KM_MAILISSA = 1.609;   /* muunnosvakio vakiomuuttujana, parempi tapa */

int main(void)
{
    double mailit,      /* etäisyys maileissa */
    kilometrit;         /* etäisyys kilometreissä */

    /* Luetaan sisään etäisyys maileissa */
    printf("Anna etäisyys maileissa >");
    scanf("%lf", &mailit);

    /* muuta etäisyys kilmetreiksi */
    kilometrit = KM_MAILISSA * mailit;

    /* tulosta etäisyys kilometreissä */
    printf("Etäisyys on %lf kilometriä", kilometrit);

    return 0;
}
