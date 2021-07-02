from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=58752958944-8q2v1e9blo1k93rl2gs3ncgmq7g1njhi.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Faffinity.co%2Fauth%2Fgoogle-oauth-callback&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.send&state=%7B%22ap%22%3A%7B%22k%22%3A%22organization-login%22%2C%22oid%22%3A8693%7D%2C%22csrf_token%22%3A%22c8aaef5b0a990720d9a45fbb15b2e2727f8c89315aecbdd120949652e6464aba%22%7D&access_type=offline&include_granted_scopes=true&prompt=select_account&flowName=GeneralOAuthFlow')

