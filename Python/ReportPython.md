(venv) PS C:\Coding\SM Assiment1\Python> pylint main.py
************* Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:3:0: C0115: Missing class docstring (missing-class-docstring)
main.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:21:12: W0719: Raising too general exception: Exception (broad-exception-raised)
main.py:23:0: C0115: Missing class docstring (missing-class-docstring)
main.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:32:40: W0622: Redefining built-in 'str' (redefined-builtin)
main.py:37:0: C0115: Missing class docstring (missing-class-docstring)
main.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:50:12: W0719: Raising too general exception: Exception (broad-exception-raised)
main.py:53:0: C0115: Missing class docstring (missing-class-docstring)
main.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:58:15: W0718: Catching too general exception Exception (broad-exception-caught)
main.py:58:8: W0612: Unused variable 'e' (unused-variable)
main.py:61:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:65:15: W0718: Catching too general exception Exception (broad-exception-caught)
main.py:65:8: W0612: Unused variable 'e' (unused-variable)
main.py:68:0: C0115: Missing class docstring (missing-class-docstring)
main.py:72:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:68:0: R0903: Too few public methods (1/2) (too-few-public-methods)
main.py:75:0: C0115: Missing class docstring (missing-class-docstring)
main.py:78:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:75:0: R0903: Too few public methods (1/2) (too-few-public-methods)
main.py:81:0: C0115: Missing class docstring (missing-class-docstring)
main.py:82:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:81:0: R0903: Too few public methods (1/2) (too-few-public-methods)
main.py:87:0: C0115: Missing class docstring (missing-class-docstring)
main.py:91:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:96:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:100:0: C0115: Missing class docstring (missing-class-docstring)
main.py:101:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:105:4: C0116: Missing function or method docstring (missing-function-docstring)
main.py:109:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 5.76/10


--
(venv) PS C:\Coding\SM Assiment1\Python> flake8 main.py
main.py:3:1: E302 expected 2 blank lines, found 1
main.py:23:1: E302 expected 2 blank lines, found 1
main.py:37:1: E302 expected 2 blank lines, found 1
main.py:50:80: E501 line too long (94 > 79 characters)
main.py:53:1: E302 expected 2 blank lines, found 1
main.py:58:9: F841 local variable 'e' is assigned to but never used
main.py:65:9: F841 local variable 'e' is assigned to but never used
main.py:68:1: E302 expected 2 blank lines, found 1
main.py:75:1: E302 expected 2 blank lines, found 1
main.py:81:1: E302 expected 2 blank lines, found 1
main.py:87:1: E302 expected 2 blank lines, found 1
main.py:100:1: E302 expected 2 blank lines, found 1
main.py:114:1: E305 expected 2 blank lines after class or function definition, found 1
--


Update:

(venv) PS C:\Coding\SM Assiment1\Python> flake8 main.py
(venv) PS C:\Coding\SM Assiment1\Python> pylint main.py
************* Module main
main.py:97:0: R0903: Too few public methods (1/2) (too-few-public-methods)
main.py:109:0: R0903: Too few public methods (1/2) (too-few-public-methods)
main.py:121:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------------------------------------
Your code has been rated at 9.65/10 (previous run: 9.53/10, +0.12)
