#include<stdio.h>

struct myArray
{
    int total_size;
    int used_size;
    int *ptr;
};

void createArray(struct myArray* a, int totalSize, int usedSize){
    (*a).total_size = totalSize
}

int main()
{
    struct myArray marks;
    createArray(&marks, 100, 20);
    
    return 0;
}