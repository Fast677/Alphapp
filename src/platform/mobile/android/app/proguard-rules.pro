# Add project specific ProGuard rules here.
# By default, the flags in this file are appended to flags specified
# in /path/to/android-sdk/tools/proguard/proguard-android.txt
# You can edit the include path and order by changing the ProGuard
# include property in project.properties.

# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html


# Mantén las anotaciones de la biblioteca de soporte de Android
-keepattributes *Annotation*

# Mantén los nombres de clases y métodos para las clases anotadas con @Keep
-keep @androidx.annotation.Keep class * { *; }

# Mantén los nombres de clases y métodos para las clases anotadas con @Keep en bibliotecas de terceros
-keep @com.google.firebase.database.IgnoreExtraProperties class * { *; }
