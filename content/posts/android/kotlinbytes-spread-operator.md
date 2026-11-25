---
title: "KotlinBytes: The Spread(*) Operator"
date: 2025-01-04T14:42:00+05:30
categories: ["Kotlin", "Android"]
tags: ["kotlin", "vararg", "spread-operator", "kotlinbytes"]
aliases: ["/2025/01/kotlinbytes-spread-operator-saviour-of.html"]
ShowToc: true
---
I have posted a similar article on a different style on linked-in which is a 2 min read, and it tries to cut to the point without any jibber jabbers ;) feel free to check it out ([here is the link](https://www.linkedin.com/pulse/refactoring-smarter-kotlins-vararg-spread-operator-simplified-r-saisc/?trackingId=MnAI3H%2BfS%2F%2B2yrXHgKJHCA%3D%3D)).

Since you have taken the long path with interest to the full story lets dive in, The current item of the sprint at work was offline-implementation for the feature i am already working on, so i had an implementation already for bulk get call for the list screen, and what i wanted is same exact implementation but this time for the detail screen so a single get call, Like most people i started to duplicate the function and modify the param and tweak the implementation to match the new requirement but then i kinda realised that i will have to modify this later as i move further, so i kinda looked around the internet and couldn't find any right solution except passing it as a list with only one item, this felt really wrong.

I tried asking ChatGPT and she gave me complicated solutions which i did not like or understand, i thought why not use varargs with the type T and just convert the list to an array, since thats exactly what varargs are internally so i decided to try it out and for the SINGLE GET it worked gracefully but for BULK GET i tried to convert it to a typed array but the lint slapped a `Type mismatch` error (inferred `Array<T>` when expecting `T` or `vararg` elements individually).

Now that's a dead end is what i thought, but before let me check with ChatGPT for a solution, and voila i discovered the [Spread Operator in Kotlin](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs), and definitely like me many may have no clue about this operator and if enlightened they could effectively refactor their code base better as this avoids the need of duplicate code let that be 5 lines of code or 50 then hell yeah we do it!

Here is something i did not discuss on the other small article that is useful (later added it), reserved to the special reader ;) though it does the magic, there is a minor setback for this approach.

As you might already know vararg is a special type and it takes in single item, multiple items or arrays as we discussed above but the thing is it can also be empty. Look at what happens when you call a `vararg` function with no arguments:

```kotlin
fun fetchItems(vararg ids: String) {
    // If called as fetchItems(), ids is an empty Array<String>
}
```

Im sure you did, yeah since the lint and compiler will be quiet if i don't pass any argument then it could silently carry a bug, but it can be easily debugged though you won't be able to enforce it, but mostly all of us are conscious coders 😆 so lets hope no one messes this up..

Hope this article was helpful and you found it insightful, if there are issues or suggestions you are most welcome to share it below or via DM ([eknath.dev](https://eknath.dev/)) :)

Thanks for reading the raw content this far ✨

---

*Note: This article was originally published on Blogger on January 4, 2025 and imported to MangoDriod.*
