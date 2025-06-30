@echo off

echo =================================================================================
echo .bat file for creating a pip package
echo =================================================================================
echo:
echo Step 1. Old pip package directories and files will be removed.
echo Step 2. Old local pip package will be removed.
echo Step 3. New pip package will be created.
echo Step 4. New package will be checked.
echo Step 5. Local installed packages will be displayed.
echo:
echo =================================================================================

echo:
echo:
echo =================================================================================
echo Step 1. Old pip package directories and files will be removed.
echo =================================================================================
cd ..
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q src\DataComparerLibrary.egg-info
rmdir /s /q src\DataComparerLibrary\__pycache__

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)

echo:
echo:
echo =================================================================================
echo Step 2. Old local pip package will be removed.
echo =================================================================================
echo:
pip uninstall DataComparerLibrary

echo:
echo:
echo =================================================================================
echo Step 3. New pip package will be created.
echo =================================================================================
echo:
pip install .
python -m build

echo:
echo:
echo =================================================================================
echo Step 4. New package will be checked.
echo =================================================================================
echo:
twine check dist/*

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)

echo:
echo:
echo =================================================================================
echo Step 5. Local installed packages will be displayed.
echo =================================================================================
echo:
pip list

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)

echo:
echo:
echo =================================================================================
echo Step 6. Upload to pypy.org.
echo =================================================================================
echo:
echo 1. Upload to https://pypi.org/
echo 2. Upload to https://test.pypi.org/
echo 3. No upload (default)
echo:
set /p choice= "Please Select one of the above options :"
echo:

if %choice%==1 (
    echo 1. Upload to https://pypi.org/
    twine upload --verbose --repository pypi dist/* -u __token__
) else if %choice%==2 (
    echo 2. Upload to https://test.pypi.org/
    twine upload --verbose --repository testpypi dist/* -u __token__
) else (
    echo 3. Geen upload.
)

echo:
echo:

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)