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

## Homepage
* This is what you will see after go to the server base directory
<img width="1648" alt="image" src="https://github.com/I-Sheng/yugabyteTest/assets/91582709/8433b0c1-20cd-4dde-93b4-04b593b53e6d">
* You can walk around with the navigate bar to add movie page or movie list page

## Add Movie Page
* Upload your movie here
<img width="1619" alt="image" src="https://github.com/I-Sheng/yugabyteTest/assets/91582709/5c302193-0c17-497d-b2c9-b19382813ec9">

## Movie list Page
* List all the movie in the database. You can go to the movie while directly press the title.
<img width="1604" alt="image" src="https://github.com/I-Sheng/yugabyteTest/assets/91582709/739a7b4f-5051-43d5-9107-92b07281334b">




