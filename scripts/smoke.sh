#!/bin/bash
adb install -r android/app/build/outputs/apk/debug/app-debug.apk || { echo "SMOKE: INSTALL FAILED"; exit 1; }
adb shell pm grant com.argosa.fitness android.permission.POST_NOTIFICATIONS || echo 'SMOKE: could not grant notifications'
adb logcat -c
adb shell am start -W -n com.argosa.fitness/.MainActivity
sleep 20
if adb shell pidof com.argosa.fitness >/dev/null; then echo "SMOKE: APP RUNNING"; else echo "SMOKE: APP NOT RUNNING"; fi
adb logcat -d > logcat.txt
echo "---- crash lines ----"
grep -E "TF-NOTIF|TF-DIAG|FATAL EXCEPTION|AndroidRuntime|Process: com.argosa|Caused by|Uncaught|Capacitor/Console|chromium.*CONSOLE" logcat.txt | head -60
echo "---- alarms ----"
adb shell dumpsys alarm | grep -c "com.argosa.fitness" || true
adb shell dumpsys alarm | grep -i "TimedNotificationPublisher" | head -3
echo "---- end ----"
adb shell pidof com.argosa.fitness >/dev/null || exit 1
