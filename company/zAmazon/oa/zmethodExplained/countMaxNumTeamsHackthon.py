#https://www.fastprep.io/problems/count-max-num-teams



'''

Amazon is hosting a team hackathon.

1. Each team will have exactly teamSize developers.
2. A developer's skill level is denoted by skill[i].
3. The difference between the maximum and minimum skill levels within a team cannot exceed a threshold, maxDiff.
Determine the maximum number of teams that can be formed from the contestants.

Complete the function countMaxNumTeams which has the following parameters

int skill[n]: the developers' skill levels
int teamSize: the number of developers to make up a team
int maxDiff: the threshold value.
int: the maximum number of teams that can be formed at one time

public int countMaxNumTeams(int[] skill, int teamSize, int maxDiff) {
    // Sort the skills in ascending order
    Arrays.sort(skill);
    int n = skill.length;
    int teamsFormed = 0;
    int i = 0;

    // Iterate through the skills array to form teams
    while (i + teamSize - 1 < n) {
        // Check if the current window can form a valid team
        if (skill[i + teamSize - 1] - skill[i] <= maxDiff) {
            teamsFormed++;  // Increment the count of teams formed
            i += teamSize;  // Move the index to attempt forming the next team
        } else {
            i++;  // Shift the window by one to check the next possibility
        }
    }

    return teamsFormed;
}


'''

def countMaxNumTeams(skills:list[int],teamSize:int,maxDiff:int):
    skills.sort()
    n = len(skills)
    teamCount = 0
    i = 0

    while i + teamSize - 1 < n:
        if skills[i + teamSize - 1]  - skills[i] <= maxDiff:
            teamCount += 1
            i += teamSize
        else:
            i += 1

    return teamCount

skill = [3, 4, 3, 1, 6, 5]
teamSize = 3
maxDiff = 2

print(countMaxNumTeams(skill,teamSize,maxDiff))