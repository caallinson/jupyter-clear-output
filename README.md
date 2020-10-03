# jupyter-clear-output
Python script to clear output cells from Jupyter notebook
(Note: notebook must be saved in JSON format with `.ipynb` extension)

Use: `jupyter-clear-output.py <notebook file>` 

Optional flag: `-f` to force run on files without `.ipynb` extension

Use this to clear outputs from Jupyter notebooks before commiting to Git.

Add `jupyter-clear-output.py` to `.git\hooks\` and the below to `.git\hooks\pre-commit`:

`shopt -s nullglob`

`for i in **/*.ipynb; do`

`	python ./.git/hooks/jupyter-clear-output.py $i`

`done`

`git add .`