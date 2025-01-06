@echo off
chcp 65001 > nul
setlocal
echo @echo off > "%~dp0/deactivate_conanrunenv-release.bat"
echo echo Restoring environment >> "%~dp0/deactivate_conanrunenv-release.bat"
for %%v in (OPENSSL_MODULES) do (
    set foundenvvar=
    for /f "delims== tokens=1,2" %%a in ('set') do (
        if /I "%%a" == "%%v" (
            echo set "%%a=%%b">> "%~dp0/deactivate_conanrunenv-release.bat"
            set foundenvvar=1
        )
    )
    if not defined foundenvvar (
        echo set %%v=>> "%~dp0/deactivate_conanrunenv-release.bat"
    )
)
endlocal


set "OPENSSL_MODULES=C:\Users\aleon\.conan2\p\opens197ef57959d34\p\lib\ossl-modules"