# https://www.fastprep.io/problems/amazon-maximize-solar-powered-bulbs

#没见过 估计不会出。以防万一
'''
Solar power consumption has increased due to concern over global warming. Some Amazon offices have decided to replace some of their electricity-powered bulbs with solar-powered bulbs. Here electricity-powered means using a wired supply of electricity and solar-powered means powered by an independent solar panel.

In one such office, the lights are arranged sequentially represented by a binary sequence, bulbs. The electricity-powered bulbs are represented by '0', and the solar powered bulbs are '1'.

It is desired to have as many solar-powered bulbs as possible, but the electricity-powered ones are brighter than the solar powered bulbs. An electricity-powered bulb can be replaced by a solar-powered bulb only if the new solar-powered bulb is not adjacent to a solar-powered bulb. More formally, a 0 can be replaced by a 1 if and only if it does not become adjacent to some other 1 on replacement.

Find the maximum number of solar powered bulbs that can be placed in the office. Note that the initial lighting may already have some adjacent solar powered bulbs. The constraint is only for new bulbs.

Note: Report the total number of solar powered bulbs and not just the number of replaced bulbs.

public int maximizeSolarPoweredBulbs(String bulbs) {
    // write your code here
    char[] bulbsArray = bulbs.toCharArray();
    int count = 0;
    for(int i=0; i<bulbsArray.length; i++) {
        char bulb = bulbsArray[i];
        char prev = '0';
        char next = '0';
        if(i>0) {
          prev = bulbsArray[i-1];
        }
        if(i<bulbsArray.length-1) {
          next = bulbsArray[i+1];
        }

        if(bulb=='1'){
            count++;
        } else {
            if(prev!='1' && next!='1') {
                count++;
                bulbsArray[i] = '1';
            }
        }
    }
    return count;
}
'''