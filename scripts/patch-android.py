import re,sys
p='android/app/src/main/AndroidManifest.xml'
s=open(p).read()
s=s.replace('<application','<queries><package android:name="com.google.android.apps.healthdata"/></queries>\n    <uses-feature android:name="android.hardware.camera" android:required="false"/>\n    <application',1)
s=s.replace('</application>','''<activity-alias android:name="ViewPermissionUsageActivity" android:exported="true" android:targetActivity=".MainActivity" android:permission="android.permission.START_VIEW_PERMISSION_USAGE">
            <intent-filter><action android:name="android.intent.action.VIEW_PERMISSION_USAGE"/><category android:name="android.intent.category.HEALTH_PERMISSIONS"/></intent-filter>
        </activity-alias>
    </application>
    <uses-permission android:name="android.permission.health.READ_STEPS"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.USE_EXACT_ALARM"/>
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>''',1)
s=s.replace('</activity>','''<intent-filter><action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE"/></intent-filter>
        </activity>''',1)
open(p,'w').write(s)
v='android/variables.gradle'
t=open(v).read()
t=re.sub(r'minSdkVersion = \d+','minSdkVersion = 26',t)
t=re.sub(r'compileSdkVersion = \d+','compileSdkVersion = 34',t)
t=re.sub(r'targetSdkVersion = \d+','targetSdkVersion = 34',t)
open('android/gradle.properties','a').write('\nandroid.suppressUnsupportedCompileSdk=34\n')
open(v,'w').write(t)
print(s)

# --- TurnFit launcher icon + splash screen ---
import shutil
shutil.copytree('android-res','android/app/src/main/res',dirs_exist_ok=True)
bg='android/app/src/main/res/values/ic_launcher_background.xml'
open(bg,'w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#0A0A0A</color>\n</resources>\n')

# --- black system bars to match the app ---
sx='android/app/src/main/res/values/styles.xml'
t=open(sx).read()
t=t.replace('<item name="android:background">@null</item>','<item name="android:background">@null</item>\n        <item name="android:statusBarColor">#000000</item>\n        <item name="android:navigationBarColor">#000000</item>\n        <item name="android:windowLightStatusBar">false</item>',1)
open(sx,'w').write(t)
