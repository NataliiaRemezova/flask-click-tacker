# Click Tracker Flask Project

This is a simple Flask Project that I created for a university assignment.

## Overview

The Click Tracker Flask Projet is a small web application created during the assignment 01 using Python and Flask in the backend and HTML and JavaScript in the frongtent. 
The web page that displays "Hello World!" and has two buttons:
   - A button "click!", that records a click (POST request to `/clicks`).
   - A button "update!", that updates and displays the list of the timestamps of the clicks in the textarea (GET request to `/clicks`).
Getting and displaying the click timestamps is done using RESTful API.


## Prerequisites

To run the web application, you will need to install
- Python
- Flask
Also Poetry was used during the development for dependencies management and virtual environment.

## Usage

1. Clone this repository.

2. Run the Flask application, using:

   ```bash
   python main.py
   ```

3. Access the web service in your web browser at `http://localhost:5000`.

4. On the web page, you can click the "click!" button to record the timestamp of a click, and the "update!" button to display the recorded click timestamps in the textarea.

5. You can also interact with the RESTful API by sending HTTP requests to the endpoints:
   - `POST /clicks`: To record a click timestamp.
   - `GET /clicks`: To get the list of recorded click timestamps.

## Example

For example, you can send a POST request to `http://localhost:5000/clicks` with a JSON object like this:

```json
{
    "timestamp": 1697394668
}
```

This will record a click timestamp. Then, sending a GET request to `http://localhost:5000/clicks` will get the list of recorded click timestamps.
