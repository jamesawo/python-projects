# Author Commenter

This is a Python script that adds author comments in the files in a given directory. It currently supports these file extension

-   .java

This script is currently updating to accept more file types in the future.

## How it works

The script takes two arguments: the author metadata and the file path to the main directory.

-   name: the name of the author
-   email: the email address of the author
-   date: the date of creation or modification of the file
-   description: a brief description of the file or the project

The file path should be a valid path to a directory that contains .java files.

```java
/*
 * Author: name
 * Email: email
 * Date: date
 * Description: description
 */
```

## How to use it

To use the script, you need to have Python 3 installed on your system.

To run the script, open a terminal or command prompt and navigate to the directory where the script is located. Then type the following command:

```bash
python author-commenter.py metadata.json file-path
```

Replace `metadata.json` with the name of your JSON file and `file-path` with the path to the main directory.

```bash
python author-commenter.py metadata.json path/to/directory
```

The script will then scan the directory and add author comments to the files. You can check the output by opening the files in any text editor or IDE.

## Feedback and Suggestions

Email me: [james.aworo@outlook.com](#)
