================================================================
PPA

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
python3.12 --version   # Output: Python 3.12.0

=================================================================
FROM SOURCE

sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

mkdir ./python && cd ./python

wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0b3.tgz

tar -xvf Python-3.12.0b3.tgz

# You need to perform tests and optimizations before installing Python.
# This is important as it increases the execution speed of your code by
# at least 10 percent:
cd Python-3.12.0b3

./configure --enable-optimizations

# Build the package using the MakeFile present in the directory:
sudo make install

=================================================================
PIP (to install packages and manage virtual enviroments,
     preinstalled python is needed)

sudo apt update && sudo apt upgrade
python3 -V
python -m pip --version
            
sudo apt install -y python3-pip
pip --version
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv

mkdir environments
cd environments
python3 -m venv myvenv # create virt env myenv
ls myvenv              # bin  include  lib  lib64  pyvenv.cfg

source myvenv/bin/activate     # activating virt env
deactivate env1/bin/activate   # deactivating virt env

pip install requests  # The "requests" library is a popular Python
		      # package for making HTTP requests and 
		      # working with APIs.
pip show requests     # show information	      
pip freeze            # list installed libraries
pip freeze > requirements.txt
pip install -r requirements.txt             # Using pip
python -m pip install -r requirements.txt   # Using python -m pip

======================================================================
PYENV
# install pyenv from:
https://github.com/pyenv/pyenv-installer

# install python:
pyenv install -l      # list all available versions
pyenv versions        # list installed versions
pyenv install 3.9.5   # install python
pyenv install 3.10.8
pyenv install 3.11.0

# create virtual enviroment with python 3.10.8:
pyenv local 3.10.8        # Set the Default Version for the Directory
pyenv virtualenv myenv1   # create virt env with version 3.10.8
python -V                 # Python 3.10.8
pyenv versions            # list installed versions
cat .python-version       # 3.10.8

# the same:
pyenv virtualenv 3.9.5 myenv2
pyenv local myenv2        # Set the Default Version for the Directory
python -V                 # Python 3.9.5  
pyenv versions            # list installed versions     
cat .python-version       # 3.9.5 

pyenv activate myenv1
python -V                 # Python 3.10.8 
pyenv deactivate myenv1   # deactivating virt env
pyenv deactivate 3.10.8   # the same
 
python -V                 # Python 3.9.5
pyenv uninstall myenv1    # uninstall virtual env
pyenv uninstall 3.11.0    # uninstall python version
pyenv versions            # check

pyenv local 3.9.5         # switch python version
pyenv local 3.10.8        

pyenv global 3.9.5        # if into directory don't set local python
python -V                 # version wil be invoke this version

pyenv local --unset

pip install requests  # The "requests" library is a popular Python
		      # package for making HTTP requests and 
		      # working with APIs.
pip show requests     # show information	      
pip freeze            # list installed libraries
pip freeze > requirements.txt
pip install -r requirements.txt

=====================================================================
IPYTHON  (https://ipython.readthedocs.io/en/stable/interactive/tutorial.html)

pip install ipython
ipython   # to start
# output:
In [6]: print('hello \nworld')
hello 
world

In [7]: 21 * 2
Out[7]: 42
