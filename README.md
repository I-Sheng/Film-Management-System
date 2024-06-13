# YugabyteTest

1. Install YugabyteDB and start it
   - [Here is the guide](https://docs.yugabyte.com/preview/quick-start/docker/)
2. Install requirements

   ```shell
   pip3 install -Ur requirements.txt
   ```

3. Make migraions

   ```shell
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. Run the server

   ```python3
   python3 manage.py runserver
   ```

## Endpoints

1. /movie
2. /add_movie
3. /admin (need to register an account first)

## Register Account
    ```python3
    python3 manage.py createsuperuser
    ```
