python_version=$(cat .python-version)

init: # install conda virtual env
	conda create -n sampleApp python=$$(cat .python-version)

install: # install all the requirements pacakge
	pip3 install -r requirements.txt
app: # start the app
	flask run
