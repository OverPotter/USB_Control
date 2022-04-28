@if (0 == 1) @end /*
@cscript //E:JScript //Nologo %~f0
@exit /B %ERRORLEVEL%
*/
var shell = new ActiveXObject("Shell.Application");
shell.NameSpace(17).ParseName("E:").InvokeVerb("Eject");
WSH.Sleep(2000);