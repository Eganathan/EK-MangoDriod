---
title: "Designer PDF Viewer - HackerRank Problems"
date: 2022-02-12T21:55:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "hackerrank", "problem-solving"]
aliases: ["/2022/02/designer-pdf-viewer-hackerrank-problems.html"]
ShowToc: true
---
##### Difficulty: EASY

##### Problem :

The objective here is to find the size of the highlighted area, and we are given the sizes of all the alphabets, we have to find the largest alphabet in the highlighted word and then calculate the size of the rectangle so if the tallest character is 3 then the size of the box will be 3 * number of characters given. Visual representation of the selection :

`[abc]` `[def]` `[ghij]`

#### Inputs

1. An array with the sizes of all alphabets a-z in order.
2. A String of highlighted words.

#### Important points to note

- **The array which holds the height of each character in ascending order**
which means the arrays 0th index will have the height of a 1st index will have the height of b and so on and so forth in the end the height of z will be there so it's easy to locate each character.
- **A String with the highlighted word.**
This means we have got the characters inside the rectangle, all we have to find is the tallest one and half our problem is solved, here we need some knowledge of ASCII representation of characters—if not I recommend you go through that first and then join again.
- **All the alphabets inside the String are lower case.**
This means the ASCII values of the characters will start from 97 so if we decrement this value from the characters of the string we will get their index.
- **Only the tallest matters to us**
With the value from the array's index, we need only the tallest in the range of our characters inside the string, so we need only the highest value. for example, if our String is `"abc"` and the array's values are `{5,3,1,9..}` we take only 5 coz it's the tallest of our string **which** is at index 0.
- **We need to return the size of the rectangle.**
Once we get the tallest character then we can multiply it by the length of the given String.

#### Algorithm

- Initialize a variable tallest to zero
- Loop through the character inside the given string
- Inside the loop Initialize a variable index
- Set the value of the index to the value - 97 (here value is the current character)
- Compare the value from the ArrayList.get(index) to tallest
- Update tallest if the value is greater.
- Return tallest multiplied words length after the loop.

#### Below is the code implementation.

```java
public static int designerPdfViewer(List <Integer> h, String word) {
    int tallest = 0;

    for (char c : word.toCharArray()) {
        int index = c - 97;
        if (h.get(index) > tallest)
            tallest = h.get(index);
    }

    return tallest * word.length();
}
```

---

*Note: This article was originally published on Blogger on February 12, 2022 and imported to MangoDriod.*
