REM =================================================================================
REM .bat file for creating a pip package
REM =================================================================================
REM
REM Step 1. Old pip package directories and files will be removed.
REM Step 2. Old local pip package will be removed.
REM Step 3. New pip package will be created.
REM Step 4. New package will be checked.
REM Step 5. Local installed packages will be displayed.
REM
REM =================================================================================

REM =================================================================================
REM Step 1. Old pip package directories and files will be removed.
REM =================================================================================
cd ..
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q src\DataComparerLibrary.egg-info
rmdir /s /q src\DataComparerLibrary\__pycache__

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)

REM =================================================================================
REM Step 2. Old local pip package will be removed.
REM Step 3. New pip package will be created.
REM Step 4. New package will be checked.
REM =================================================================================
pip uninstall DataComparerLibrary
pip install .
python -m build
twine check dist/*

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)

REM =================================================================================
REM REM Step 5. Local installed packages will be displayed.
REM =================================================================================
pip list

set "dummy="
set /p DUMMY=Hit ENTER to continue...
if defined dummy (echo not just ENTER was pressed) else (echo just ENTER was pressed)