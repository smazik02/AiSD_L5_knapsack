#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int** genItems(int n) {
    int** items = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        items[i] = malloc(3 * sizeof(int));
    }
    for (int i = 0; i < n; i++) {
        items[i][0] = i + 1;
        items[i][1] = (rand() % 9) + 1;
        items[i][2] = (rand() % 9) + 1;
    }
    return items;
}

char* binConvert(int num) {
    char* result = malloc((int)floor(log2(num)) + 2);
    int* temp = malloc((floor(log2(num)) + 1) * sizeof(int));
    int i;
    for (i = 0; num > 0; i++) {
        temp[i] = num % 2;
        num /= 2;
    }
    int j = 0;
    for (i = i - 1; i >= 0; i--) {
        result[j++] = temp[i];
    }
    result[j++] = '\0';
    return result;
}

int getRatio(int* list) {
    return list[2] / list[1];
}

char* bruteForce(int** items, int cap, int size) {
    int max = 0, massSum = 0, valSum = 0, sum = 0;
    char* solution = malloc(size + 1), knapsack = malloc(size + 1);
    for (int i = 0; i < size; i++) {
        solution[i] = '0';
    }
    solution[size] = '\0';
    for (int i = 1; i <= pow(2, size); i++) {
        knapsack = binConvert(i);
    }
    return solution;
}

int main(void) {
    srand(time(NULL));
    int** arr = genItems(5);
    for (int i = 0; i < 5; i++) {
        printf("Item %d, weight %d, value %d\n", arr[i][0], arr[i][1], arr[i][2]);
    }
    return 0;
}