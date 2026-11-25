---
title: "Implementing In-app and pre-locale language selection in Android"
date: 2024-01-14T16:13:00+05:30
categories: ["Android"]
tags: ["android", "localization", "in-app-language"]
aliases: ["/2024/01/blog-post.html"]
ShowToc: true
---
![](/img/blogger/blog-post-1.png)

One of the essential features for a globalized app is the ability to provide users with the option to choose their preferred language within the application. In this blog post, we will guide you through the process of implementing in-app language selection in an Android app.

## Step 1: Create Locale String Resource

Create a string resource file for each respective locale by navigating to `res > new > Android Resource File` . Select Locale and create a `string.xml` file. Copy and paste the translations of your app content into these files.

## Step 2: Configure Locale Preferences

In the `res/xml` folder, create a new file called `locales_config.xml` and specify the locales of your choice. for example look at the following code:

```xml
<?xml version="1.0" encoding="utf-8"?>
<locale-config xmlns:android="http://schemas.android.com/apk/res/android">
    <locale android:name="en" /> //English
    <locale android:name="ta" /> //Tamil
    <locale android:name="hi" /> //Hindi
    <locale android:name="ml" /> //Malayalam
</locale-config>
```

## Step 3: Add resources.properties file

Switch to project view and in the `res` folder, create a new file called `resources.properties` and specify the default locales of your choice, this will be the fallback locale if the requested one is unavailable, for example look at the following code:

```kotlin
unqualifiedResLocale=en
```

## Step 4: Update Module Gradle File

The list of language tags needs to be added to `resourceConfigurations` make sure you add all the language tags, have shared the updated code below as per my sample app:

```kotlin
android {
    ...
    androidResources {
        generateLocaleConfig = true
    }
    ...
    defaultConfig {
        ...
        resourceConfigurations.plus(listOf("ta", "en", "hi", "your-language-tag"))
    }
}
```

## Step 5: Manifest Configuration

You can let the device handle the locales, for that we are going to use a service called `androidx.appcompat.app.AppLocalesMetadataHolderService` with the following configuration, you can just copy paste the following code

```xml
<application ...>
    <service
        android:name="androidx.appcompat.app.AppLocalesMetadataHolderService"
        android:enabled="false"
        android:exported="false">
        <meta-data
            android:name="autoStoreLocales"
            android:value="true" />
    </service>
</application>
```

## Step 6: Implement Locale Selection Function

```kotlin
fun localeSelection(context: Context, localeTag: String) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        context.getSystemService(LocaleManager::class.java).applicationLocales =
            LocaleList.forLanguageTags(localeTag)
    } else {
        AppCompatDelegate.setApplicationLocales(
            LocaleListCompat.forLanguageTags(localeTag)
        )
    }
}
```

## Step 7: Usage Example

```kotlin
val context = LocalContext.current
Button(onClick = {
    localeSelection(context = context, localeTag = Locale("ta").toLanguageTag())
}) {
    Text(text = "Tamil")
}
```

That's it! You've successfully implemented in-app language selection in your Android app. Feel free to check out the [sample app on GitHub](https://github.com/Eganathan/Compose-LocalizationSample) for a hands-on example.

If you encounter any issues or have questions, please leave a comment, and will do my best to assist you.

---

*Note: This article was originally published on Blogger on January 14, 2024 and imported to MangoDriod.*
