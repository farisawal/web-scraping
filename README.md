# web-scraping

## The url of scraping website is https://subway.com.my/find-a-subway

This repo is a code to scrape the information about the store location and their respective details.
To achieve this, I use the selenium library to access selenium WebDriver. It can automate the interaction of the website. This library is choose because the scraping website has a complex structure which is dynamic and need user interaction to get any output.
There is also other library such as BeautifulSoup, and Scrappy. But, for this task, selenium is capable to do the task.

Selenium Documentation: https://selenium-python.readthedocs.io/

## How to Run

To run this application, firstly we need to have the required library and dependecies. The list of library can be look through the requirements.txt file.

1. Run the cmd command to create virual env (optional, but preferred):
   ```
   py -3.11 -m venv .\
   \Scripts\activate
   ```
2.  install dependacies:
  ```
  pip install -r requirements.txt
  ```

3. launch the jupyter notebook:
  ```
  jupyter lab
  ```
4. run the python script to run API
   ```
   python location_api.py
   ```

