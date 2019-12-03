
# LibDoc2Json
Small python class which converts Robot Framework Libdoc XML Files to JSON that is compatible with VSCode plugin "Robot Framework Intellisense"

**Installation**:

    pip install robotframework-libdoc2json

**Usage**:

    python -m libdoc2json <LIBRARY or *.robot or *.py> <MyLibrary.json>

The generated json file might be put o this folder and then be set up in settings.json of vscode.

    "rfLanguageServer.libraries": 
    [
        "BuiltIn-3.0.4",
        "SeleniumLibrary-3.2.0",
        "Dialogs-3.0.4",
        {<put the generated json into this list>}
    ]
    

It is possible to just put the complete JSON into the rfLanguageServer.libraries List.
