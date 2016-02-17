#plug in device
#https://kivyspacegame.wordpress.com/2014/06/30/tutorial-how-to-build-python-for-android-with-ubuntu-and-buildozer/

buildozer -v android debug
cp bin/MyApplication-0.1-debug.apk /home/kwatson/Android/Sdk/platform-tools
cd /home/kwatson/Android/Sdk/platform-tools/
adb install MyApplication-0.1-debug.apk
