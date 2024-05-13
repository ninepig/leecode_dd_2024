#https://www.fastprep.io/problems/amazon-execute-processes
'''
Amazon Web Services (AWS) has several processors for executing processes scheduled on its servers.

There are n processes to be executed, where the ith process takes execution[i] amount of time to execute.
Two processes are cohesive if and only if their original execution times are equal. When a process with execution time execution[i] is executed, it takes execution[i] time to complete and simultaneously reduces the execution time of all its cohesive processes to ceil(execution[i] / 2).

Given the execution time of n processes, find the total amount of time the processor takes to execute all the processes
if you execute the processes in the given order, i.e. from left to right.

'''
import copy

'''
 public static int totalExecutionTime(int[] execution) {
        // write your code here
        HashMap<Integer, HashSet<Integer>> map = new HashMap<>();
        int[] copy = Arrays.copyOf(execution, execution.length);

        for(int i = 0; i < execution.length; i++){
            int num = execution[i];
            if(!map.containsKey(num)){
                map.put(num, new HashSet<>());
            }

            map.get(num).add(i);
        }

        int res = 0;
        for(int i = 0; i < execution.length; i++){
            int num = copy[i];
            //System.out.println(num);
            res += num;
            int half = num / 2;
            int originalNum = execution[i];
            HashSet<Integer> set = map.get(originalNum);
            for(Integer index : set){
                if(index > i){
                    copy[index] -= half;
                }
            }
        }

        return res;
    }

'''
import collections
import math
def totalTime(excution:list[int])->int:
    map = collections.defaultdict(set)
    copy_array = copy.deepcopy(excution) ## 问题在这里
    for idx,value in enumerate(excution):
        map[value].add(idx)
    total_time = 0
    for i in range(len(excution)):
        cur_value = copy_array[i]
        total_time += cur_value
        original_key = excution[i]
        cur_set = map[original_key]
        for val in cur_set: ## update same value's spot to half
            copy_array[val] = math.ceil(copy_array[val]/2) ## it equal to get the ceil of half
        copy_array[i] = 0
        print(copy_array)
    return total_time


test = [5, 5, 3, 6, 5, 3]
print(totalTime(test))