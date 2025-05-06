#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void saxpy(int n, float a, float x[], float y[], float result[]) {
    for (int i = 0; i < n; i++) {
        result[i] = a * x[i] + y[i];
    }
}

int main() {
    int sizes[] = {32768, 65536, 131072, 262144, 524288, 1048576, 2097152};
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    
    for (int s = 0; s < num_sizes; s++) {
        int N = sizes[s];
        float *x = (float *)malloc(N * sizeof(float));
        float *y = (float *)malloc(N * sizeof(float));
        float *result = (float *)malloc(N * sizeof(float));
        float a = 2.0f;

        for (int i = 0; i < N; i++) {
            x[i] = 1.0f;
            y[i] = 2.0f;
        }

        clock_t start = clock();
        saxpy(N, a, x, y, result);
        clock_t end = clock();
        double time_spent = (double)(end - start) / CLOCKS_PER_SEC * 1000;

        printf("N = %d, Time = %.4f ms\\n", N, time_spent);

        free(x);
        free(y);
        free(result);
    }
    return 0;
}
