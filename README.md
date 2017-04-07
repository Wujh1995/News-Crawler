# News-Crawler
A Python script to crawl down news from school`s website and mail to you through SMTP Protocol
It`s for static website.

**Contains 2 files:**
- **crawl.py**  The main file that you should run after configuring;
- **iMessage.py**  Contains a function, to send e-mail to you.

# Steps to configure:
**In crawl.py:**
- At the top of the code, web1/web2/web3/web4 are the websites to crawl, you may change these to whatever you want.
  - At the bottom, there are a main function and a 'Run' function, if you change the number of websites that to be crawled, you should change these code too.

**In iMessage.py:**
- Change the 'mail_info' to adapt your need.
- "hostname" mustn`t change; "from" must be same to "username"; you may use your own tencent smtp user account, or mine, as you like.

Ps. You may download BeautifulSoup before running the script, it contains the 'bs4' library, which is nessesary.

Anyway, it`s not a complicated code that you can surely understand every line even you are a beginner.

And if you are a Sun Yet-sen University`s student, you may use it with nothing to change but the mail receiver.

If you suffered enough the black frame when running the script and want it run in back-stage, you may type the following command.

Under Windows cmd:
>> start pythonw crawl.py

Under Linux terminal:
$ python crawl.py &

Then the annoying black frame will not appear again.

**simple_version.py** is a simple all-in-one version for new learners, it crawls only one website.
