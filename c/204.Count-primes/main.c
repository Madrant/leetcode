#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int n = 10;

    // Init prime array
    int is_prime[n];

    for (int i = 0; i < n; i++)
    {
        is_prime[i] = 1;
    }

    // 0 and 1 are not primes
    is_prime[0] = 0;
    is_prime[1] = 0;

    // Filter values not primes values
    for (int i = 2; i * i < n; i++)
    {
        printf("i: %i\r\n", i);

        if (is_prime[i] == 0) continue;

        for (int j = i * i; j < n; j += i)
        {
            printf(" j: %i", j);

            is_prime[j] = 0;
        }
        printf("\r\n");
    }

    // Count primes
    int count = 0;

    for (int i = 0; i < n; i++)
    {
        if (is_prime[i] == 1) count++;
    }

    printf("count: %i\r\n", count);

    return 0;
}
