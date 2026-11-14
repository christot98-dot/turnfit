import re,sys
p='android/app/src/main/AndroidManifest.xml'
s=open(p).read()
s=s.replace('<application','<queries><package android:name="com.google.android.apps.healthdata"/></queries>\n    <uses-feature android:name="android.hardware.camera" android:required="false"/>\n    <application',1)
s=s.replace('</application>','''<activity-alias android:name="ViewPermissionUsageActivity" android:exported="true" android:targetActivity=".MainActivity" android:permission="android.permission.START_VIEW_PERMISSION_USAGE">
            <intent-filter><action android:name="android.intent.action.VIEW_PERMISSION_USAGE"/><category android:name="android.intent.category.HEALTH_PERMISSIONS"/></intent-filter>
        </activity-alias>
    </application>
    <uses-permission android:name="android.permission.health.READ_STEPS"/>
    <uses-permission android:name="android.permission.CAMERA"/>''',1)
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
