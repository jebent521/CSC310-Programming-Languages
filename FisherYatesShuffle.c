/*
    Jonah Ebent, 9/19/23
    FisherYatesShuffle.c, CSC 310 Programming Languages, Dr. Coleman
    Shuffles an array by implementing the Fisher-Yates Shuffle algorithm
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int shuffle(int[], int);

int main(void) {
    srand(time(NULL));                                  // seed the random function
    int SIZE = 10;

    int arr[SIZE];                                      // create array and fill it with numbers in ascending order
    for(int i=0; i<SIZE; i++) arr[i] = i;

    for (int i=0; i<SIZE; i++) printf("%d ", arr[i]);   // print array
    printf("\n");

    shuffle(arr, SIZE);                                 // shuffle array

    for (int i=0; i<SIZE; i++) printf("%d ", arr[i]);   // print array
    printf("\n");
}

int shuffle(int arr[], int len) {
    for(int i=0; i<len-1; i++) {                        // for each element in array, except last
        int j = i + rand() % (len - i);                     // select random integer between i and len
        int temp = arr[i];                                  // swap arr[i] and arr[j]
        arr[i] = arr[j];
        arr[j] = temp;
    }
}