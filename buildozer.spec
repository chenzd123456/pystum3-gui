[app]

# (str) Title of your application
title = STUN Checker

# (str) Package name
package.name = stunchecker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pystun3

# (str) Custom source folders for requirements
#requirements.source = 

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY2

# (str) The directory in which python/kivy source files are stored
#fullscreen = 0

# (str) Android logcat filters to use
#logcat_filters = *:S python:D

# (bool) Copy the whole directory recursively into the package
#android.copy_libs = 1

# (str) Android entry point
#android.entrypoint = org.renpy.android.PythonActivity

# (str) iOS deploy target
#ios.deploy_target = 9.0

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (list) Android additional libraries to copy into libs/armeabi-v7a
#android.add_libs_armeabi_v7a = libs/android-v7/*.so

# (list) Android additional libraries to copy into libs/arm64-v8a
#android.add_libs_arm64_v8a = libs/android-v8/*.so

# (list) Android additional libraries to copy into libs/x86
#android.add_libs_x86 = libs/android-x86/*.so

# (list) Android additional libraries to copy into libs/x86_64
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (list) Android additional libraries to copy into libs/mips
#android.add_libs_mips = libs/android-mips/*.so

# (list) Android additional libraries to copy into libs/mips64
#android.add_libs_mips64 = libs/android-mips64/*.so

# (list) Android additional Java classes to add to the project
#android.add_java_classes = 

# (list) Android aar inclusions (build dependencies)
#android.add_aars = 

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support (default is false)
#android.enable_androidx = False

# (bool) Enable Android fullscreen mode
#android.fullscreen = False

# (str) Android app theme
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Permissions
#android.permissions = INTERNET

# (list) Android compileSdkVersion
#android.compile_sdk_version = 28

# (list) Android buildToolsVersion
#android.build_tools_version = 28.0.3

# (int) Android API to use
#android.api = 28

# (int) Minimum Android API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use private storage (Android only)
#android.private_storage = False

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
#android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) Android additional permissions
#android.permissions = 

# (str) Android logcat filters to use
#logcat_filters = *:S python:D

# (bool) Copy library sources instead of symlinking
#android.copy_libs = 1

# (str) The name of the keystore to use for signing the APK
#android.keystore = 

# (str) The alias to use for signing the APK
#android.keystore.alias = 

# (str) The password for the keystore
#android.keystore.password = 

# (str) The password for the alias
#android.keystore.alias.password = 

# (str) The path to the keystore
#android.keystore.path = 

# (str) The algorithm to use for signing
#android.keystore.algorithm = 

# (str) The digest algorithm to use for signing
#android.keystore.digest = 

# (int) Override Android platform
#android.platform = 

# (str) Android NDK version to use
#android.ndk = 

# (str) Android SDK version to use
#android.sdk = 

# (str) Android build tools version to use
#android.build_tools_version = 

# (bool) If True, then build a debug version of the APK
#android.debug = False

# (bool) If True, then build a release version of the APK
#android.release = False

# (str) The command to use to launch the app
#android.adb = 

# (bool) If True, then automatically install the APK
#android.auto_install = False

# (bool) If True, then automatically uninstall the APK
#android.auto_uninstall = False

# (bool) If True, then automatically start the app
#android.auto_start = False

# (bool) If True, then automatically stop the app
#android.auto_stop = False

# (bool) If True, then automatically clear the app data
#android.auto_clear = False

# (bool) If True, then automatically grant permissions
#android.auto_grant = False

# (bool) If True, then automatically revoke permissions
#android.auto_revoke = False
