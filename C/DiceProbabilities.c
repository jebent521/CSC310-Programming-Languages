/*
    Jonah Ebent, 9/16/23
    DiceProbabilities.c, CSC 310 Programming Languages, Dr. Coleman
    Estimates the probability of getting a given sum when rolling a pair of dice
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));                                  // seed the random function
    for (int target = 2; target <= 12; target++) {      // traverse through possible sums (targets)
        int successes = 0;
        for (int count = 0; count < 10000; count++) {
            int die_1 = 1 + rand() % 6;                 // roll two dice
            int die_2 = 1 + rand() % 6;

            if (die_1 + die_2 == target) successes++;   // if sum equals target, increment successes
        }
        printf("%d = %f\n", target, successes/10000.0); // print results
    }
}