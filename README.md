# plagiarism-checker-server

### Prerequisites
* Install Python
* Install Python Package Manager (pip/pip3) :
    ```
    apt-get install python-pip
    ```
    ```
    apt-get install python3-pip
    ```
* Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) :
    ```
    apt-get install virtualenv
    ```

### Project Installation

1. Clone the repository - `git clone <remote-url>`
2. Go to the project directory - `cd <cloned-repo>`
3. Set up the environment :
    * Create virtual environment files - `virtualenv -p python3 venv`
    * Activate virtual environment - `source venv/bin/activate`
4. Install dependencies - `pip3 install -r requirements.txt`
6. Copy contents of `.env.example` to a new file `.env` - `cp .env.example .env`
7. Make migrations - `python3 manage.py makemigrations`
8. Run migrations - `python3 manage.py migrate`
9. Start server - `python3 manage.py runserver`

#### Note
* Everytime you install packages or run the server, activate your virtual environment - `source venv/bin/activate`
* To deactivate the activated virtual environment - run the command `deactivate` in terminal.
* If you ran into any errors while running the server with python version incompatabilities, try `python3` instead of `python` while running the server.
* If you install any python packages, please update the file `requirements.txt`

### Contributing

See [Developer's Guide](https://github.com/avikumar15/plagiarism-checker-server/wiki) in the Wiki.
