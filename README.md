# Twitter-Sentiment-Analyzer

Twitter's API is annoying to work with, and has lots of limitations. Scrape all the tweets using simple python and selenium - No API rate limits. No restrictions. Extremely fast.

## Average Tweets 

It appears you can ask for up to 25 pages of tweets reliably (~1200 tweets)

## Dependencies

    * selenium
    * vaderSentiment
    * chromedriver-install

## Dependencies Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following
```bash
pip install -r requirements.txt
```

## Usage

Download it by clicking the green download button here on Github. You only need to parse argument specific Twitter keyword.
```bash
python main.py --keyword 'petta'

or

python main.py -k 'petta'
```

## Output

![capture](https://user-images.githubusercontent.com/47944792/53886316-c3002b00-4045-11e9-8a56-10ef06275951.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
