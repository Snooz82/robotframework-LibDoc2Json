
check-manifest --update
del dist\* /Q /S /F
python setup.py bdist_wheel sdist
pause
twine check dist/*
pause
twine upload dist/* --username snooz82 --password "u]y#l7&X4slC*FD*Zxc1+5ou?q0SVZAzdZg]}:L5A5n?v@:4]fW3vmEeRE,LUI?H"