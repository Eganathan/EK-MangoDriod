---
title: "Breaking the Records - HackerRank- Problem Solving in Java"
date: 2022-01-30T12:36:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "hackerrank", "problem-solving"]
aliases: ["/2022/01/breaking-records-hackerrank-problem.html"]
ShowToc: true
---
##### Difficulty : EASY

##### Problem :

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

#### Visual representation of the table

<table>
<tr>
<th>Game</th>
<th>Score</th>
<th>Minimum</th>
<th>Maximum</th>
<th>Count Min</th>
<th>Count Max</th>
</tr>
<tr>
<td>0</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td>24</td>
<td>12</td>
<td>24</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>10</td>
<td>10</td>
<td>24</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>24</td>
<td>10</td>
<td>24</td>
<td>1</td>
<td>1</td>
</tr>
  <tr>
    <th colspan="2">Output :</th>
    <td colspan="4">[1 , 1]</td>
  </tr>
</table>

### Important Points to note

- We calculate the record determining her performance on Game 0 which will be the value of minimum and maximum.
- We change the value of maximum or minimum only if her score breaks our current record of maximum or minimum.
- in case she breaks record then we increment the counter respectively.
- return the Count max and Count min in the same order as a List.

### Algorithm

- inputs received : `List<Integer> score, int games`
- Set Min and Max to scores 1st element or 0th index element.
- Loop through the scores from the 2nd element or the 1st index till the scores.size()-1
- inside the above loop check if the value of current index is larger than maximum if so then increase the counter of the maximum and set the value of the maximum to the current value.
- else if statement to check if the value is smaller than current minimum if so then increase the counter of the minimum and set the value of minimum to the current value
- outside the loop create an array and add the two values in the order of maxcount then min count and add the list to the return statement.

**I Highly recommend you dont go through the below code now but try to solve it on your own to build the ability to solve problems, but im just pasting it here for those who haven't managed to find the solution despite many tries**

```java
List<Integer> breakingTheRecords(List<Integer> score) {
    int currentMax = score.get(0);
    int currentMin = score.get(0);

    int surpassed = 0;
    int backlogged = 0;

    for (int index = 1; index < score.size(); index++) {
        if (score.get(index) > currentMax) {
            surpassed++;
            currentMax = score.get(index);
        } else if (score.get(index) < currentMin) {
            backlogged++;
            currentMin = score.get(index);
        }
    }

    List<Integer> result = new ArrayList<>();
    result.add(surpassed);
    result.add(backlogged);
    System.out.println(surpassed + " " + backlogged);
    return result;
}
```

---

*Note: This article was originally published on Blogger on January 30, 2022 and imported to MangoDriod.*
