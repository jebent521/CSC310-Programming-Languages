/*
    Jonah Ebent, 9/29/23
    100PrisonersProblem.c, CSC 310 Programming Languages, Dr. Coleman
    Monte-Carlo simulation of the 100 Prisoners' Problem to demonstrate probability of success is ~31%
*/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 100
#define ITERATIONS 100000

void initializeRoom(int[], int);    // initialize the room with a random permutation of 1-SIZE
bool findNumber(int, int[], int);   // given a prisoner number and room, determine if prisoner finds number in at most 50 steps
int testRoom(int[], int);           // given a room, determine if all prisoners find their numbers (returns 1 if successful, 0 if not)

int main(void) {
    srand(time(NULL));                      // seed random number generator

    int successes = 0;
    for(int i=0; i<ITERATIONS; i++) {       // loop through iterations
        int room[SIZE];                         // create array room
        initializeRoom(room, SIZE);             // fill it with values and shuffle them
        successes += testRoom(room, SIZE);      // test room and modify successes accordingly
    }
    // display results
    printf("Did %d iterations of room size %d.\n", ITERATIONS, SIZE);
    printf("There were %d successes, with a success rate of %f.\n", successes, successes/(float)ITERATIONS);
}

void initializeRoom(int room[], int roomSize) {
    for(int i=0; i<roomSize; i++) room[i] = i+1;    // initialize with elements 1-100 in order
    // Fisher-Yates Shuffle
    for(int i=0; i<roomSize-1; i++) {               // for each element in array, except last
        int j = i + rand() % (roomSize - i);            // select random integer between i and len
        int temp = room[i];                             // swap arr[i] and arr[j]
        room[i] = room[j];
        room[j] = temp;
    }
}

bool findNumber(int prisonerNumber, int room[], int roomSize) {
    int maxAttempts = roomSize/2;                           // set maximum allowable attempts to roomSize/2
    int attemptCount = 1;                                   // initialize attempt counter to 1
    int boxToCheck = prisonerNumber - 1;                    // first box to check (index) is the prisoner's number
    
    while(attemptCount <= maxAttempts) {                    // while attempts are less than max attempts,
        if(room[boxToCheck] == prisonerNumber) return true;     // if prisoner finds his number, return true
        boxToCheck = room[boxToCheck] - 1;                      // otherwise, set box to check to contents of the box just checked
        attemptCount++;                                         // increment attemptCount
    }
    return false;                                           // if loop exits without finding number, return false
}

int testRoom(int room[], int roomSize) {
    for(int i=1; i<=roomSize; i++){                  // for each prisoner (1-100)
        if(!findNumber(i, room, roomSize)) return 0;    // try to find number; if unsuccessful, return 0
    }
    return 1;                                       // if loop ends without failure, return 1
}
