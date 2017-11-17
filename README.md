# CSCI375_Top_Comment
By: Will Burford, Vincent Lin, Haoyu Sheng, Tongyu Zhou

Our goal is to develop a YouTube comment generator, which will generate the top comment on a given YouTube video. On the way to this goal, we will create a classifier which will quantify the probability of a comment getting the most likes on a given video.

## Package and Data Management
### Setup
To setup your local environment, run:
```
$ make
```
This will create a virtual environment in, stored in `venv`, and install all dependencies listed in `requirements.txt`. It will also extract the relevant files from `youtube.zip` into `youtube/` (these files are `US_category_id.json`, `UScomments.csv`, and `USvideos.csv`). After this, you must activate the virtual environment by running:
```
$ source venv/bin/activate
```
You must run this last command every time you start a new terminal session so that you will be in the virtual environment and have the correct package versions!

#### TLDR
On initial setup, run:
```
$ make
$ source venv/bin/activate
```
Run the second command every time you open a new terminal session.

### Cleaning
To clean your local directory of your virtual environment and un-zipped data files, run:
```
$ make clean
```
You will now be able to re-initialize your environment. If cleaning fails, make sure that your virtual environment has been deactivated. It is active if you see `(venv)` at the beginning of the line in terminal. To deactivate the virtual environment, run:
```
$ deactivate
```
You can then retry running `make clean`.
