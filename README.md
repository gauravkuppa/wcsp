Top K Solutions Generator
------------------------

1. Compile `wcsp-solver` (The README file contains instructions).
2. Run `main.py` to generate top K solutions of a given WCSP instance. The path of input file (with DIMACS format, example can also be found in the `wcsp-solver` folder) and the path to the binary of the solver are necessary.
3. Run `python main.py -h` to understand the parameters.



## Installing toulbar2

### Installing require dependencies
sudo apt-get install libgmp-dev libboost-graph-dev libboost-iostreams-dev zlib1g-dev liblzma-dev libxml2-dev libopenmpi-dev libjemalloc-dev -y

### Download and installation

#### Clone the toulbar2 repo
git clone https://github.com/toulbar2/toulbar2.git <br />
cd toulbar2 <br />
mkdir build <br />
cd build <br />
'# ccmake ..' <br />
cmake .. <br />
make <br />

#### Install toulbar2
echo "deb http://ftp.fr.debian.org/debian sid main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install toulbar2

### Run NQueens
Go into NQueens.py and update the variable 'toulbar2Path' with path to toulbar2 folder
Run NQueens.py


