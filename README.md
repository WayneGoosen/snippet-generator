# Snippet Generator

This is a Python Flask web application which helps create code snippets for a Visual Studio Code Extension or your local global user snippets.   

[![Build Status](https://travis-ci.org/WayneGoosen/snippet-generator.svg?branch=master)](https://travis-ci.org/WayneGoosen/snippet-generator)
[![Coverage Status](https://coveralls.io/repos/github/WayneGoosen/snippet-generator/badge.svg)](https://coveralls.io/github/WayneGoosen/snippet-generator)

## VS Code Snippet

The current JSON structure of a VS Code snippet is as follows:

```json
"basic_property": {
	"prefix": "b-prop",
	"description": "Basic property snippet.",
	"body": [
		"_busy: {",
		"\t\ttype: Boolean",
		"}"
	]
},
```

## Usage

### Basic

Enter your code in the text area below 'Enter Code' and click Submit. The generated snippet will be outputted to the 'Generated Snippet' text area.

#### Advanced

The 'Advanced Configuration' allows input for Key, Description, Prefix, Line Endings and Tab Size. Input your advanced configuration along with your code and click Submit. The generated snippet will be outputted to the 'Generated Snippet' text area.

## Creating Snippets

Please see the [Visual Studio Documentation - Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## Run the app locally (MacOS)

- Clone the repo.
- Navigate into the project.
- Run the following commands:

```Batchfile
# Setup virtual environment (install virtualenv if you dont have it)
virtualenv env
source env/bin/activate

# Install all requirements
pip install -r requirements.txt

# Run the app with gunicorn
gunicorn run:app;
```

## Contributing

Please fork the branch, create a new feature branch, add your changes and push. Submit a pull request :)

## License

[MIT License](https://github.com/WayneGoosen/snippet-generator/blob/master/LICENSE)