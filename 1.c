#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int read_file(char* filename, char** ret_data){
    int fd = open(filename, O_RDONLY);
    char* data = (char*)malloc(1);
    int buflen = 1;
    int index = 0;
    char c;
    while(read(fd, &c, 1) != 0){
        data = realloc(data, buflen + 1);
        buflen += 1;
        data[index++] = c;
    }
    data[index] = '\0';
    close(fd);
    *ret_data = data;
    return buflen;
}


int split_string(char* string, char delimiter, char*** split_strings){
    char** parts = (char**)malloc(sizeof(char*));
    int last_delim = -1;
    int cur_part = 0;
    for(int i = 0; i < strlen(string); i++){
        if(string[i] == delimiter){
            parts = realloc(parts, (cur_part+1)*sizeof(char*));
            char* part = (char*)malloc(i-last_delim);
            strncpy(part,string+last_delim+1, i - last_delim - 1);
            part[(i - last_delim) - 1] = '\0';
            parts[cur_part++] = part;
            last_delim = i;
        }
    }
    *split_strings = parts;
    return cur_part;
}

void free_array_of_strings(char** array_of_strings, int list_len){
    for(int i = 0; i < list_len; i++){
        free(array_of_strings[i]);
    }
    free(array_of_strings);
}

int split_array_of_strings(char** array, int array_len, char* delimiter, char**** split_arrays, int** array_lengths){
    char*** parts = (char***)malloc(sizeof(char**));
    int* arr_lens = (int*)malloc(sizeof(int));
    int last_delim = -1;
    int cur_part = 0;
    for(int i = 0; i < array_len; i++){
        if(strcmp(array[i], delimiter) == 0 || i == array_len - 1){
            int array_length = i - last_delim - !(i == array_len - 1);
            arr_lens = (int*)realloc(arr_lens, (cur_part+1)*sizeof(int));
            arr_lens[cur_part] = array_length;
            parts = (char***)realloc(parts, (cur_part+1)*sizeof(char**));
            char** part = (char**)malloc(array_length*sizeof(char*));
            for(int j = 0; j < (array_length); j++){
                char* element = (char*)malloc(strlen(array[j+last_delim+1]));
                strcpy(element, array[j+last_delim+1]);
                part[j] = element; 
            }
            last_delim = i;
            parts[cur_part++] = part;
        }
    }
    *split_arrays = parts;
    *array_lengths = arr_lens;
    return cur_part;
}

int sum_group(char** group, int length){
    int sum = 0;
    for(int i = 0; i < length; i++){
        sum += atoi(group[i]);
    }
    return sum;
}

int max(int* vals, int length){
    int cmax = vals[0];
    for(int i = 0; i < length; i++){
        if(vals[i] > cmax) cmax = vals[i];
    }
    return cmax;
}

void part1(){
    char* file_contents;
    int length = read_file("input.txt", &file_contents);
    char** lines;
    int n_lines = split_string(file_contents, '\n', &lines);

    char*** groups;
    int* group_lengths;
    int num_groups = split_array_of_strings(lines, n_lines, "\0", &groups, &group_lengths);
    
    int* sums = (int*)malloc(num_groups*sizeof(int));
    for (int i = 0; i < num_groups; i++){
        sums[i] = sum_group(groups[i], group_lengths[i]);
        free_array_of_strings(groups[i], group_lengths[i]);
    }
    printf("%i\n", max(sums, num_groups));
    free(groups);
    free(group_lengths);
    free(file_contents);
    free_array_of_strings(lines, n_lines);
}
int main(){
    part1();
    return 0;

}