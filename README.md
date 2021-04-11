# Prerequisites
- Linux, macOs, Windows
- Python 3

# Getting Started
###  Installation
```bash
git clone https://github.com/sam5727/shorten-url.git
cd shorten-url
```
###  Activate virtual environment
```bash
python -m venv shoten-url-env
# On Windows, run
# shoten-url-env\Scripts\activate.bat
# On Unix or MacOS, run
# source tutorial-env/bin/activate
```
Check more detail on [venv](https://docs.python.org/3/tutorial/venv.html)

### Setup
```bash
pip install -r requirements.txt
uvicorn shorten_url.main:app --reload
```
After setting up, we can simply test the RESTful on http://localhost:8000/docs, which is provided by FastAPI.

### Test
```bash
pytest -rA
# And the report will be like
# ============================ test session starts =============================
# platform win32 -- Python 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
# rootdir: C:\Users\sam5727\Desktop\shorten-url
# collected 5 items

# shorten_url\test_main.py .....                                          [100%]

# =================================== PASSES =================================== 
# ========================== short test summary info =========================== 
# PASSED shorten_url/test_main.py::test_register_invalid_url
# PASSED shorten_url/test_main.py::test_register_url
# PASSED shorten_url/test_main.py::test_register_existed_url
# PASSED shorten_url/test_main.py::test_redirect_url_not_found
# PASSED shorten_url/test_main.py::test_register_and_redirect_to_shortened_url
# ============================= 5 passed in 0.45s ============================== 

```
