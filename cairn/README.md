# CAIRN

"Chuirinn clach air a chairn," "I would put a stone on his cairn" is a Gaelic phrase said in symbolism to the feelings of respect and honour felt to one who has parted from this life, a statement implying that he will be remembered, that he is worthy of being remembered. In Gaelic culture, the living are connected to the dead. The dead are those who came before us, who gave us our upbringing and our heritage. This web application addresses the reality of death and is named after an image that respects the dead. This is appropriate because these topics of conversation should not be side stepped, but met directly. CAIRN is an OPENAI API chatbot web application designed to give young men a safe and secluded space to explore and navigate their mind and feelings. It was created to address the high suicide rates in men.


## Table of Contents

- [File Directory](#file-directory)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## File Directory

+ cairn/
    + _pycache_/
        + app.cpython-39.pyc 
        + app.cpython-312.pyc
    + static/
        + cairn_logo.png
        + 20210803_112356.jpg
        + main.css
    + templates/
        + index.html
    + .env
    + .gitignore
    + app.py
    + database.py
    + db_test.py
     + init_db.py 
    + LICENSE
    + README.md
    + requirements.txt


## Installation

Ensure that you have [Git](https://git-scm.com/download/) and [Python](https://www.python.org/downloads/) 3.9 or higher installed before starting the installation process. Also ensure that you have configured the OpenAI key (see [here](https://platform.openai.com/docs/quickstart?context=python) for instructions). It is also best practice to create a virtual environment (see [here](https://docs.python.org/3/library/venv.html) for instructions).

1. **Clone the repository**: type `git clone https://github.com/FraochGeal/CAIRN.git` in the command prompt
2. **Navigate to the project directory**: type `cd cairn`
3. **Install the required dependencies**: type `pip install -r requirements.txt`
4. **Setup the database by executing**: type `python init_db.py`
5. **Check environment variables**: ensure the .env file contains `FLASK_APP`, `FLASK_ENV`, and the `OPENAI_API_KEY`
6. **Run the application**: type `flask run`
7. **Access the application in a web browser**: navigate to http://localhost:5000
8. **To stop the application**: type `Ctrl + C` in the command prompt window.


## Usage

CAIRN is a mental health app design for young men to explore their feelings. To get started, follow these steps:

1. **Type Message**: After accessing CAIRN (see [Installation](#installation)), you will see a form on the homepage. Type your message and press enter.
2. **Review Response**: After submission, a response generated by OPEN AI API will appear in the chatbox.
3. **Continue Conversation**: Continue chatting with the OPEN AI chatbot for as long as desired.


## Contributing

1. **Fork and clone**: Fork the repository to your GitHub account and clone it locally.
2. **Create a new branch**: Before making changes, create a dedicated branch for your changes.
3. **Make your changes**: Implement your new feature.
4. **Push changes to your fork**: Update your forked repository on GitHub with your branch.
5. **Submit a pull request**: Open a pull request with a comprehensive description of your changes for review by the project maintainers.


## License

This project is licensed under the [MIT License]. Please see the [LICENSE](./LICENSE) file for full license terms.
