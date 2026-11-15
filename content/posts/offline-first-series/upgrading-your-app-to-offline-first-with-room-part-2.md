---
date: '2025-02-10T10:02:29+05:30' 
draft: false
title: 'Setting-up Room Library and its dependencies(#OF02)'
tags: ["Room","Android","Offline-First-App"]
aliases: ["/posts/upgrading-your-app-to-offline-first-with-room-part-2/"]
categories: ["Android","KMP"]
---

Before we proceed with the setup, let’s quickly recap **why** we chose Room:

✅ **Compile-time SQL Validation** – Catches errors early by verifying SQL queries at compile time.  
✅ **Kotlin-first Approach** – Supports coroutines, Flow, and LiveData natively.  
✅ **Less Boilerplate Code** – Simplifies database interactions while maintaining SQLite’s power.  
✅ **Seamless Migration Handling** – Built-in support for database migrations.  

For a more detailed explanation, refer to the [official Android documentation](https://developer.android.com/training/data-storage/room).  

---

## Official Documentation

Google keeps its documentation up to date with a simple setup guide. However, you might wonder why we need this article if the documentation is available.  

Google’s documentation caters to **both Java and Kotlin** developers, but since most of us have migrated to **Kotlin**, we don’t need Java-specific instructions. This article focuses on a **Kotlin-first approach** to setting up Room.

📖 [Official Guide on Setting up Room Dependencies and Plugins](https://developer.android.com/jetpack/androidx/releases/room).  

---

## Setting up Dependencies

### 1️⃣ Configure Project-Level `build.gradle.kts`  

Ensure your project-level `build.gradle.kts` file includes **Google’s Maven repository** and **Maven Central**, as these are where Room dependencies are hosted.

```kotlin
buildscript {
    repositories {
        google()
        mavenCentral()
    }
}
```

### 2️⃣ Add Room Dependencies

Head to your module-level build.gradle.kts file and add only the required Room dependencies inside the dependencies block:

```kotlin
dependencies {
    // Other dependencies 

    // Room Dependencies
    val room_version = "2.6.1"

    // Room Database Core
    implementation("androidx.room:room-runtime:$room_version")

    // Annotation Processor (KSP)
    ksp("androidx.room:room-compiler:$room_version")

    // Kotlin Extensions and Coroutines support for Room (Optional)
    implementation("androidx.room:room-ktx:$room_version")

}
```

🔎 Check for Latest Versions
Always use the latest stable version of Room and KSP:

📌 [Maven Central - Room Runtime](https://mvnrepository.com/artifact/androidx.room/room-runtime)
📌 [kotlin-ksp-releases](https://github.com/google/ksp/releases)

### 3️⃣ Add the Room Plugin

**Project-Level build.gradle.kts**
Add the Room plugin reference to the project-level build.gradle.kts file:

```kotlin
plugins {
    id("androidx.room") version "$room_version" apply false 
    id("com.google.devtools.ksp") version "2.0.21-1.0.27" apply false 
    // Other plugins...
}
```

**Module-Level build.gradle.kts**
Add this to the module-level `build.gradle` file:

```kotlin
plugins {
    id("androidx.room")
    id("com.google.devtools.ksp")
}
```

### 4️⃣ Configure Schema Directory

Room allows schema export for better version control and database migrations. Let’s specify a schema directory inside the android {} block:

```kotlin
android {
    ...
    room {
        schemaDirectory("$projectDir/schemas")
    }
}
```

### Sync & Verify Installation

Once you’ve added the dependencies and plugin, sync your Gradle project. If everything is set up correctly, you should have Room ready for use in our project! 🎉

```bash
./gradlew build 
```

---

### Sample Code for a quick reference

I hope you had no issues setting up the dependencies, if you need a sample app to compare the change-set feel free to checkout this [commit](https://github.com/Eganathan/jotters-space-android/commit/92613b0b3f1e08709b94752a5276d6031466e16a).

---

## **What’s Next?**  

This short article we have learned how to set-up the room dependencies to our projects and hopefully this was helpful:
📌 **In the next part of this series, we’ll dive into:**  

1️⃣ **Key Components of Room**

- **@Entity**: Defines how **data is stored** in the table.  
- **@Dao**: Specifies **how to interact** with the table (CRUD operations).  
- **@Database**: Configures the database and **associates Entities and DAOs**.

2️⃣ **How to create, access and interact with a simple database**.

---
## **Final Thoughts**  

This is my journey in **building an offline-first app**. I’d love to hear your feedback, suggestions, or questions!  

Feel free to connect with me on:  
📩 **[Email](mailto:mail@eknath.dev)**  
🌍 **[Website](https://eknath.dev)**       
💫 **[LinkedIn-Post for comments and feedbacks](https://www.linkedin.com/posts/eganathan_offlinefirstandroid-offlinefirst-android-activity-7294912159627546624-TG77?utm_source=share&utm_medium=member_desktop&rcm=ACoAABYcOpgBgvDfy-0uUjfX0HTNqzzLfKZQAQU)** 

🔖 [Previous Article in this Series]({{< relref "/posts/offline-first-series/upgrading-your-app-to-offline-first-with-room-part-1/" >}})

🔖 [Next Article in this Series]({{< relref "/posts/offline-first-series/upgrading-your-app-to-offline-first-with-room-part-3/" >}})
