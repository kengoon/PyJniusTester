# This .spec config file tells Buildozer an app's requirements for being built.
#
# It largely follows the syntax of an .ini file.
# See the end of the file for more details and warnings about common mistakes.

[app]

# (str) Title of your application
title = Pyjnius Playground

# (str) Package name
package.name = playground

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pyjnius

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (leave empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.2

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==master,pygments,androidstorage4kivy,kivymd

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/logo.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/logo.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait, landscape

# (list) List of services to declare
# This is currently only relevant to Android services.
# Each service consists of a name (a valid Java class name, with the first letter capitalized)
# followed by a colon, followed by the name of the Python script (.py file) that should be
# launched. This is optionally followed by ":foreground" for foreground services or
# ":foreground:sticky" for sticky foreground services. The default is a background service.
# Bound services are not supported.
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# Kivy version to use
osx.kivy_version = 2.2.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
#android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)
android.permissions = android.permission.ACCEPT_HANDOVER, android.permission.ACCESS_BACKGROUND_LOCATION,
    android.permission.ACCESS_CHECKIN_PROPERTIES, android.permission.ACCESS_COARSE_LOCATION,
    android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_LOCATION_EXTRA_COMMANDS,
    android.permission.ACCESS_MEDIA_LOCATION, android.permission.ACCESS_NETWORK_STATE,
    android.permission.ACCESS_NOTIFICATION_POLICY, android.permission.ACCESS_SURFACE_FLINGER,
    android.permission.ACCESS_WIFI_STATE, android.permission.ACCOUNT_MANAGER, android.permission.ACTIVITY_RECOGNITION,
    android.permission.ADD_SYSTEM_SERVICE, android.permission.ADD_VOICEMAIL, android.permission.ANSWER_PHONE_CALLS,
    android.permission.AUTHENTICATE_ACCOUNTS, android.permission.BATTERY_STATS,
    android.permission.BIND_ACCESSIBILITY_SERVICE, android.permission.BIND_APPWIDGET,
    android.permission.BIND_AUTOFILL_SERVICE, android.permission.BIND_CALL_REDIRECTION_SERVICE,
    android.permission.BIND_CARRIER_MESSAGING_CLIENT_SERVICE, android.permission.BIND_CARRIER_MESSAGING_SERVICE,
    android.permission.BIND_CARRIER_SERVICES, android.permission.BIND_CHOOSER_TARGET_SERVICE,
    android.permission.BIND_CONDITION_PROVIDER_SERVICE, BIND_CONTROLS, BIND_DEVICE_ADMIN, BIND_DREAM_SERVICE,
    android.permission.BIND_INCALL_SERVICE, android.permission.BIND_INPUT_METHOD,
    android.permission.BIND_MIDI_DEVICE_SERVICE, android.permission.BIND_NFC_SERVICE,
    android.permission.BIND_NOTIFICATION_LISTENER_SERVICE, android.permission.BIND_PRINT_SERVICE,
    android.permission.BIND_QUICK_ACCESS_WALLET_SERVICE, android.permission.BIND_QUICK_SETTINGS_TILE,
    android.permission.BIND_REMOTEVIEWS, android.permission.BIND_SCREENING_SERVICE,
    android.permission.BIND_TELECOM_CONNECTION_SERVICE, android.permission.BIND_TEXT_SERVICE,
    android.permission.BIND_TV_INPUT, android.permission.BIND_VISUAL_VOICEMAIL_SERVICE,
    android.permission.BIND_VOICE_INTERACTION, android.permission.BIND_VPN_SERVICE,
    android.permission.BIND_VR_LISTENER_SERVICE, android.permission.BIND_WALLPAPER, android.permission.BLUETOOTH,
    android.permission.BLUETOOTH_ADMIN, android.permission.BLUETOOTH_PRIVILEGED, android.permission.BODY_SENSORS,
    android.permission.BRICK, android.permission.BROADCAST_PACKAGE_REMOVED, android.permission.BROADCAST_SMS,
    android.permission.BROADCAST_STICKY, android.permission.BROADCAST_WAP_PUSH, android.permission.CALL_COMPANION_APP,
    android.permission.CALL_PHONE, android.permission.CALL_PRIVILEGED, android.permission.CAMERA,
    android.permission.CAPTURE_AUDIO_OUTPUT, android.permission.CAPTURE_SECURE_VIDEO_OUTPUT,
    android.permission.CAPTURE_VIDEO_OUTPUT, android.permission.CHANGE_COMPONENT_ENABLED_STATE,
    android.permission.CHANGE_CONFIGURATION, android.permission.CHANGE_NETWORK_STATE,
    android.permission.CHANGE_WIFI_MULTICAST_STATE, android.permission.CHANGE_WIFI_STATE,
    android.permission.CLEAR_APP_CACHE, android.permission.CLEAR_APP_USER_DATA,
    android.permission.ONTROL_LOCATION_UPDATES, android.permission.DELETE_CACHE_FILES,
    android.permission.DELETE_PACKAGES, android.permission.DEVICE_POWER, android.permission.DIAGNOSTIC,
    android.permission.DISABLE_KEYGUARD, android.permission.DUMP, android.permission.EXPAND_STATUS_BAR,
    android.permission.FACTORY_TEST, android.permission.FLASHLIGHT, android.permission.FORCE_BACK,
    android.permission.FOREGROUND_SERVICE, android.permission.FOTA_UPDATE, android.permission.GET_ACCOUNTS,
    android.permission.GET_ACCOUNTS_PRIVILEGED, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS,
    android.permission.GET_TOP_ACTIVITY_INFO, android.permission.GLOBAL_SEARCH, android.permission.HARDWARE_TEST,
    android.permission.INJECT_EVENTS, android.permission.INSTALL_LOCATION_PROVIDER, android.permission.INSTALL_PACKAGES,
    android.permission.INSTALL_SHORTCUT, android.permission.INSTANT_APP_FOREGROUND_SERVICE,
    android.permission.INTERNAL_SYSTEM_WINDOW, android.permission.INTERNET, android.permission.KILL_BACKGROUND_PROCESSES,
    android.permission.LOADER_USAGE_STATS, android.permission.LOCATION_HARDWARE, android.permission.MANAGE_ACCOUNTS,
    android.permission.MANAGE_APP_TOKENS, android.permission.MANAGE_DOCUMENTS, android.permission.MANAGE_EXTERNAL_STORAGE,
    android.permission.MANAGE_OWN_CALLS, android.permission.MASTER_CLEAR, android.permission.MEDIA_CONTENT_CONTROL,
    android.permission.MODIFY_AUDIO_SETTINGS, android.permission.MODIFY_PHONE_STATE,
    android.permission.MOUNT_FORMAT_FILESYSTEMS, android.permission.MOUNT_UNMOUNT_FILESYSTEMS, android.permission.NFC,
    android.permission.NFC_PREFERRED_PAYMENT_INFO, android.permission.NFC_TRANSACTION_EVENT,
    android.permission.PACKAGE_USAGE_STATS, android.permission.PERSISTENT_ACTIVITY,
    android.permission.PROCESS_OUTGOING_CALLS, android.permission.QUERY_ALL_PACKAGES, android.permission.READ_CALENDAR,
    android.permission.READ_CALL_LOG, android.permission.READ_CONTACTS, android.permission.READ_EXTERNAL_STORAGE,
    android.permission.READ_FRAME_BUFFER, android.permission.READ_HISTORY_BOOKMARKS, android.permission.READ_INPUT_STATE,
    android.permission.READ_LOGS, android.permission.READ_OWNER_DATA,
    android.permission.READ_PHONE_NUMBERS, android.permission.READ_PHONE_STATE,
    android.permission.READ_PRECISE_PHONE_STATE, android.permission.READ_PROFILE, android.permission.READ_SMS,
    android.permission.READ_SOCIAL_STREAM, android.permission.READ_SYNC_SETTINGS, android.permission.READ_SYNC_STATS,
    android.permission.READ_USER_DICTIONARY, android.permission.READ_VOICEMAIL, android.permission.REBOOT,
    android.permission.RECEIVE_BOOT_COMPLETED, android.permission.RECEIVE_MMS, android.permission.RECEIVE_SMS,
    android.permission.RECEIVE_WAP_PUSH, android.permission.RECORD_AUDIO, android.permission.REORDER_TASKS,
    android.permission.REQUEST_COMPANION_RUN_IN_BACKGROUND, android.permission.REQUEST_COMPANION_USE_DATA_IN_BACKGROUND,
    android.permission.REQUEST_DELETE_PACKAGES, android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS,
    android.permission.REQUEST_INSTALL_PACKAGES, android.permission.REQUEST_PASSWORD_COMPLEXITY,
    android.permission.RESTART_PACKAGES, android.permission.SEND_RESPOND_VIA_MESSAGE, android.permission.SEND_SMS,
    android.permission.SET_ACTIVITY_WATCHER, android.permission.SET_ALARM, android.permission.SET_ALWAYS_FINISH,
    android.permission.SET_ANIMATION_SCALE, android.permission.SET_DEBUG_APP, android.permission.SET_ORIENTATION,
    android.permission.SET_POINTER_SPEED, android.permission.SET_PREFERRED_APPLICATIONS,
    android.permission.SET_PROCESS_FOREGROUND, android.permission.SET_PROCESS_LIMIT, android.permission.SET_TIME,
    android.permission.SET_TIME_ZONE, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS,
    android.permission.SIGNAL_PERSISTENT_PROCESSES, android.permission.SMS_FINANCIAL_TRANSACTIONS,
    android.permission.START_VIEW_PERMISSION_USAGE, android.permission.STATUS_BAR, android.permission.SUBSCRIBED_FEEDS_READ,
    android.permission.SUBSCRIBED_FEEDS_WRITE, android.permission.SYSTEM_ALERT_WINDOW,
    android.permission.TRANSMIT_IR, android.permission.UNINSTALL_SHORTCUT, android.permission.UPDATE_DEVICE_STATS,
    android.permission.USE_BIOMETRIC, android.permission.USE_CREDENTIALS, android.permission.USE_FINGERPRINT,
    android.permission.USE_FULL_SCREEN_INTENT, android.permission.USE_SIP, android.permission.VIBRATE,
    android.permission.WAKE_LOCK, android.permission.WRITE_APN_SETTINGS, android.permission.WRITE_CALENDAR,
    android.permission.WRITE_CALL_LOG, android.permission.WRITE_CONTACTS, android.permission.WRITE_EXTERNAL_STORAGE,
    android.permission.WRITE_GSERVICES, android.permission.WRITE_HISTORY_BOOKMARKS, android.permission.WRITE_OWNER_DATA,
    android.permission.WRITE_PROFILE, android.permission.WRITE_SECURE_SETTINGS, android.permission.WRITE_SETTINGS,
    android.permission.WRITE_SMS, android.permission.WRITE_SOCIAL_STREAM, android.permission.WRITE_SYNC_SETTINGS,
    android.permission.WRITE_USER_DICTIONARY, android.permission.WRITE_VOICEMAIL

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = True

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class which extends PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (bool) If True, your application will be listed as a home app (launcher app)
# android.home_app = False

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_exts'.
# 1) android.add_assets = source_asset_relative_path
# 2) android.add_assets = source_asset_path:destination_asset_relative_path
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or zero ':'
# Some examples:
# 1) A file to add to resources, legal resource names contain ['a-z','0-9','_']
# android.add_resources = my_icons/all-inclusive.png:drawable/all_inclusive.png
# 2) A directory, here  'legal_icons' must contain resources of one kind
# android.add_resources = legal_icons:drawable
# 3) A directory, here 'legal_resources' must contain one or more directories, 
# each of a resource kind:  drawable, xml, etc...
# android.add_resources = legal_resources
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
#android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to src/main/res/xml/ (used for example with intent-filters)
#android.res_xml = PATH_TO_FILE,

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
# Valid values can be found at https://developer.android.com/guide/topics/manifest/activity-element
android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]
# android.manifest_placeholders = [:]

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# Run "buildozer android p4a -- bootstraps" for a list of valid values.
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" --use-setup-py is going to be the default behaviour in p4a, right now it is not
# Setting this to false will pass --ignore-setup-py, true will pass --use-setup-py
# NOTE: this is general setuptools integration, having pyproject.toml is enough, no need to generate
# setup.py if you're using Poetry, but you need to add "toml" to source.include_exts.
#p4a.setup_py = false

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =



#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url` options.
#ios.manifest.app_url =

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url` options.
#ios.manifest.display_image_url =

# (str) URL pointing to a large icon (512x512px) to be used by iTunes
# This option should be defined along with `app_url` and `display_image_url` options.
#ios.manifest.full_size_image_url =


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#-----------------------------------------------------------------------------
#   Notes about using this file:
#
#   Buildozer uses a variant of Python's ConfigSpec to read this file.
#   For the basic syntax, including interpolations, see
#       https://docs.python.org/3/library/configparser.html#supported-ini-file-structure
#
#   Warning: Comments cannot be used "inline" - i.e.
#       [app]
#       title = My Application # This is not a comment, it is part of the title.
#
#   Warning: Indented text is treated as a multiline string - i.e.
#       [app]
#       title = My Application
#          package.name = myapp # This is all part of the title.
#
#   Buildozer's .spec files have some additional features:
#
#   Buildozer supports lists - i.e.
#       [app]
#       source.include_exts = py,png,jpg
#       #                     ^ This is a list.
#
#       [app:source.include_exts]
#       py
#       png
#       jpg
#       # ^ This is an alternative syntax for a list.
#
#   Buildozer's option names are case-sensitive, unlike most .ini files.
#
#   Buildozer supports overriding options through environment variables.
#   Name an environment variable as SECTION_OPTION to override a value in a .spec
#   file.
#
#   Buildozer support overriding options through profiles.
#   For example, you want to deploy a demo version of your application without
#   HD content. You could first change the title to add "(demo)" in the name
#   and extend the excluded directories to remove the HD content.
#
#       [app@demo]
#       title = My Application (demo)
#
#       [app:source.exclude_patterns@demo]
#       images/hd/*
#
#   Then, invoke the command line with the "demo" profile:
#
#        buildozer --profile demo android debug
#
#   Environment variable overrides have priority over profile overrides.
