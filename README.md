# Simple Grocery List App with Flask and VueJS

### Want to learn how to build this?

Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## TO DO LIST:

- ~~create an 'initilize database' function~~
- ~~refactor app, database to match [this post](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)~~
- ~~sort grocery items by category~~
- fix bug in update button :bug:
- auto sort into category


## Want to use this project?

1. Fork/Clone

2. Set environment varible

    Enter the following in a new file: `/client/.env`
    ```sh
    VUE_APP_API_URL='http://HOST-IP:5000'
    ```

3. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    ```

4. Initialize database and start server

    From the `server` directory, run the following command:
    ```sh
    (env)$ python create_db.py
    (env)$ flask run
    ```

    At the prompt, enter Y to input some initial items or N to start with an empty database

    Navigate to [http://HOST-IP:5000/items](http://localhost:5000/items) to see all database items


4. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://HOST-IP:8080](http://localhost:8080)
