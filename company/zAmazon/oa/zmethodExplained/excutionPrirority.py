#https://www.fastprep.io/problems/get-priorities-after-execution

"""
QUESTION:
Several processes are scheduled for execution on an AWS server. On one server, n processes are scheduled where
the ith process is assigned a priority of priority[i]. the processes are placed sequentially in a queue and are
numbered 1,2,...n. The server schedules the processes per the following algorithm.

Step 1. If finds the maximum priority shared by at least 2 processes. Let that be denoted by p. If there is no such
priority or p = 0, the algorithm is terminated

Step 2. Otherwise, select the two of the processes with the lowest indexes and priority p, and call them process1
and process2.

Step 3. The server executes process1 and removes it from the queue.

Step 4. To avoid starvation, it reduces the priority of process2 to the floor(p/2).

Step 5. Start again from step 1.

Given the initial priority of the processes, find the final priority of the processes which remain after the
algorithm terminates.

Note that relative to the arrangements of the remaining processes in the queue remains the same, only their
priorities change.

Example: The number of processes n=6 and their priorities = [6,6,6,1,2,2]
"""
import collections
import heapq

''' 
public class Question2 {

  public static void main(String[] args) {
    int[] priority = new int[]{6,6,6,1,2,2};
    int[] res = getPrioritiesAfterExecution(priority);
    for(int num : res){
      System.out.println(num);
    }
  }

  public static int[] getPrioritiesAfterExecution(int[] priority){
    if(priority == null || priority.length == 0){
      return new int[0];
    }
    Map<Integer, PriorityQueue<Integer>> indexMap = new HashMap<>();
    PriorityQueue<Integer> queue = new PriorityQueue<>((a,b) -> b -a);
    for(int i = 0; i < priority.length; i++){
      if(!indexMap.containsKey(priority[i])){
        indexMap.put(priority[i], new PriorityQueue<>());
        queue.add(priority[i]);
      }
      indexMap.get(priority[i]).add(i);
    }

    while (!queue.isEmpty()){
      Integer pr = queue.poll();
      if(pr == 0){
        break;
      }
      if(indexMap.get(pr).size() < 2){
        continue;
      }
      PriorityQueue<Integer> list = indexMap.get(pr);
      int index1 = list.poll();
      int index2 = list.poll();
      if(list.size() == 0){
        indexMap.remove(pr);
      }else {
        queue.add(pr);
        indexMap.put(pr, list);
      }
      int newOne = pr/2;
      priority[index1] = Integer.MIN_VALUE;
      priority[index2] = newOne;
      if(!indexMap.containsKey(newOne)){
        indexMap.put(newOne, new PriorityQueue<>());
        queue.add(newOne);
      }
      indexMap.get(newOne).add(index2);
    }

    List<Integer> res = new ArrayList<>();
    for(int i = 0; i < priority.length; i++){
      if(priority[i] != Integer.MIN_VALUE){
        res.add(priority[i]);
      }
    }

    int[] result = new int[res.size()];
    for(int i = 0; i < res.size(); i++){
      result[i] = res.get(i);
    }
    return result;
  }

}
    
'''
## 遇到这个还是用java写吧。。简单明了。。