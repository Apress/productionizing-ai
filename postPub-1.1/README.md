# postPub-1.1
source code for Productionizing AI - new trends: Causal AI

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bw-cetech/postPub-1.1.git/HEAD)

NB for ERRORS INSTALLING DOWHY (PYWHY) PYTHON LIBRARY e.g.
Failed building wheel for shap / error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

go to link https://visualstudio.microsoft.com/visual-cpp-build-tools/ and install Microsoft Visual C++
NB install basic package (visual studio build tools 2022), then select tab "available" and install
visual studio community 2022 >
include desktop development with c++ addin
NB installing visual studio community may take a while up to half an hour

after completion, go back to virtual environment C:\ce.tech\apps\jupyter-notebooks\env-jup and reinstall:

pip install dowhy

it should successfull install shap and complete (might take another 10-15 mins)

alternatively try this:

pip install setuptools --upgrade
