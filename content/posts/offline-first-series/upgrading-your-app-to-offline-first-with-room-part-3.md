---
date: '2025-02-22T11:23:17+05:30' 
draft: false
title: 'Key Components of Room & Manually Creating A Database Instance(#OF03)'
tags: ["Room","Android","Offline-First-App"]
aliases: ["/posts/upgrading-your-app-to-offline-first-with-room-part-3/"]
categories: ["Android","KMP"]
---
## 👋 Intro

On the [previous article]({{< relref "/posts/offline-first-series/upgrading-your-app-to-offline-first-with-room-part-2/" >}}) we have set-up the Room dependencies and plugins, Now lets get into the primary key components of a room library.

There are three important components: **Entity**, **DAO**'s, and **Database**.  

- **Entity** represents a single row of a table. (Table structure)
- **DAO**'s (Data Access Objects) are interfaces to write queries and define operations.
- **Database** is where you associate entities and include the DAO's you'd like to access from outside.  

Let's check it out one by one! 🔍

---

## 🏗️ Entities: Defining Your Data Structure

Any class annotated with `@Entity` is called a entity, it represents a table in a database, while designing the entity ensure you follow [Normalizations Rules](https://www.geeksforgeeks.org/normal-forms-in-dbms/) to keep it simple and future proof. Let's look checkout a sample entity in a Habit Tracker app.

**Example:**

```kotlin
@Entity
data class LocalHabitTracker(
    @PrimaryKey(autoGenerate = true) val id: Long,
    val associatedHabitId: Long,
    val positionX: Int,
    val positionY: Int,
    val note: String
)
```

**Key Points:**    

✅ An entity **must have** at least one parameter annotated with @PrimaryKey.    
✅ The **primary key** must be unique the `primaryKey` column can't have a duplicate key.    
✅ If you want Room to **auto-generate** the primary key, set autoGenerate = true otherwise to false.    
✅ Stick to **primitive types** like Long or Int as PrimaryKey.    

The entity can be further customized with **table names, indexing, custom column names, keys and more**, which we’ll cover in next article. 🎯

## 🔗 DAOs: Your Data Gateway

DAOs or Data Access Objects serve as the interface between your app and the database, providing an abstraction layer. This is a bridge between you the developer and the Database all your interactions you intend to have table must be defined here later at compile time the compiler will generate the concrete classes for these at compile time, lets see an example how to define these interactions.

**✍️ Example:**

```kotlin
@Dao
interface HabitTrackerDao {

    // Query to get all habit trackers
    @Query("SELECT * FROM LocalHabitTracker")
    suspend fun getAll(): List<LocalHabitTracker>

    // Query to get a habit tracker by ID
    @Query("SELECT * FROM LocalHabitTracker WHERE id = :id")
    suspend fun getById(id: Long): LocalHabitTracker

    // Insert a new row into the table (fails if duplicate)
    @Insert
    suspend fun insert(habitTracker: LocalHabitTracker)

    // Update an existing row
    @Update
    suspend fun update(habitTracker: LocalHabitTracker)

    // Upsert: If exists, update; otherwise, insert
    @Upsert
    suspend fun upsert(habitTracker: LocalHabitTracker)

    // Delete a row from the table
    @Delete
    suspend fun delete(habitTracker: LocalHabitTracker)
}
```

**Best Practices:**

✅ **One entity per DAO:** It’s best to separate interaction with each table into its own DAO for maintainability.     
✅ **Keep queries optimized** to avoid performance issues as your app scales.     
✅ **Inheritance** if some of the interactions are common to other Dao's create a new Dao with `Common` as prefix for example`CommonHabitTrackerDao`.    

We’ll cover complex cases like @RawQuery, Junctions, and TableViews in later articles as to not over-complicate this! 🔮

## 🏛️ Database: The Central Hub

Now that we have defined the entities and DAOs, we need to create a database to integrate thee entity and Dao's into its domain. Now the room can effectively generate its contents when instantiated along with this the database also manages the integrity validation, migrations and works as a central hub of control for our interactions with this database and its entities.

Here is an **example** of a database class:

```kotlin
@Database(
    entities = [LocalHabitTracker::class], // Add all your entities here
    version = 1 // Update this when modifying the schema
)
abstract class HabitTrackerDataBase : RoomDatabase() {

    // Room will auto-implement this function and return the DAO implementation
    abstract fun habitTrackerDao(): HabitTrackerDao

}
```

**Important Notes:**

✅ Always increase the version when modifying entities, it enables room to validate the integrity of tables and run migrations effectively.    
✅ Room doesn’t know how to handle schema changes unless you define a migration strategy.    
✅ Multiple databases can exist in an app, so this class serves as an entry point of the particular database.   

Migrations and schema updates are crucial for real-world apps to prevent data loss. We’ll cover on later articles. 🔄

## 🎛️ Manually Creating and Using the Database

Now, let’s see how to manually create and interact with the database in our app.

**✍️ Example:**

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Creating the database manually
        val habitTrackerDB = Room.databaseBuilder(
            context = this, // ApplicationContext
            klass = HabitTrackerDataBase::class.java, // Database abstract class
            name = "habbit_tracker" // Custom database name
        ).build() 
        
        // Get the DAO implementation
        val habitTrackerDao = habitTrackerDB.habitTrackerDao()

        setContent {
            AppTheme {
                AppNav(activity = this, habitLocalService = habitTrackerDao)
            }
        }
    }
}
```

**⚡ Pro Tips:**

✅ Don’t use the UI thread for database operations; always use coroutines or background threads.    
✅ In real-world apps, use Dependency Injection (DI) for managing database instances efficiently.     
✅ Avoid creating multiple database instances, as it can lead to memory leaks and performance issues.    

Mostly this is enough for creating simple CRUD apps, though it looks simple the entities will be converted into a query to create tables, A concrete classes will be created for each Dao's and other essential tasks will be carried by room it self easing our development and debug process.

## 🚀 What’s Next?

This was a quick run through of some of the key components of room, on the next article we will dive a little deeper into **@Entity** its keys and customizations,as we have a larger purpose to explore them each in detail.

## **Final Thoughts**  

This is my journey in **building an offline-first app**. I’d love to hear your feedback, suggestions, or questions!  

Feel free to connect with me on:  
📩 **[Email](mailto:mail@eknath.dev)**  
🌍 **[Website](https://eknath.dev)** 
💫 **[LinkedIn-Post for comments and feedbacks](https://www.linkedin.com/posts/eganathan_offlinefirstandroid-offlinefirst-android-activity-7294912159627546624-TG77?utm_source=share&utm_medium=member_desktop&rcm=ACoAABYcOpgBgvDfy-0uUjfX0HTNqzzLfKZQAQU)** 

🔖 [Previous Article in this Series]({{< relref "/posts/offline-first-series/upgrading-your-app-to-offline-first-with-room-part-2/" >}})


🔖 [Next Article in this Series]({{< relref "/posts/offline-first-series/upgrading-your-app-to-offline-first-with-room-part-4/" >}})
