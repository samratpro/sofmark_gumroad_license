; Define installer name and output directory
[Setup]
AppName=Fish Dealer Software 6.5
AppVersion=6.5
DefaultDirName={localappdata}\FishDealerSoftware_6.5
DefaultGroupName=Fish Dealer Software 6.5
OutputBaseFilename=FishDealerSetup_6.5
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\logo.ico

; Wizard images (if needed)
WizardImageFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\appbanner.bmp
WizardSmallImageFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\logo.bmp

; Silent installation option
DisableDirPage=no
DisableProgramGroupPage=yes

; Include Python interpreter and app files
[Files]
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\python\*"; DestDir: "{app}\python"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\font\*"; DestDir: "{app}\font"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\icons\*"; DestDir: "{app}\icons"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\images\*"; DestDir: "{app}\images"; Flags: recursesubdirs

; Create necessary folders
[Dirs]
Name: "{app}"; Permissions: everyone-full
Name: "{localappdata}\FishDealerSoftware"; Permissions: everyone-full

; Registry settings (optional)
[Registry]
Root: HKCU; Subkey: "Software\FishDealerSoftware2"; Flags: uninsdeletekey

; Shortcuts
[Icons]
[Icons]
Name: "{group}\Fish Dealer Software"; Filename: "{app}\python\app.exe"; Parameters: """{app}\app.py"""; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"
Name: "{group}\Uninstall Fish Dealer Software"; Filename: "{uninstallexe}"; IconFilename: "{app}\static\logo.ico"
Name: "{commondesktop}\Fish Dealer Software"; Filename: "{app}\python\app.exe"; Parameters: """{app}\app.py"""; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"

; Run the application after installation
[Run]
Filename: "{app}\python\app.exe"; Parameters: """{app}\app.py"""; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent

; Uninstaller (removes everything)
[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{localappdata}\FishDealerSoftware"

; Optional tasks
[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked