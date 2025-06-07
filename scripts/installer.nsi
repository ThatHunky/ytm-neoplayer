; YT Music Player NSIS installer
OutFile "ytm-neoplayer-installer.exe"
InstallDir "$PROGRAMFILES\\YT Music Player"
Page directory
Page instfiles
Section "Main" SecMain
  SetOutPath $INSTDIR
  File "dist\\ytm-neoplayer.exe"
  CreateShortCut "$DESKTOP\\YT Music Player.lnk" "$INSTDIR\\ytm-neoplayer.exe"
SectionEnd
