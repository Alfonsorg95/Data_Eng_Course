import argparse
import logging
from urllib.parse import urlparse
import pandas as pd
import hashlib
import nltk
from nltk.corpus import stopwords

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
stop_words = set(stopwords.words('spanish'))

def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df, newspaper_uid)
    df = _extract_host(df)
    df = _strip_column(df, 'body')
    df = _generate_rows_uids(df)
    df['title words'] = _tokenize_column(df, 'title')
    df['body words'] = _tokenize_column(df, 'body')

    return df


def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('uid detected: {}'.format(newspaper_uid))
    return newspaper_uid


def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))

    df['newspaper uid'] = newspaper_uid

    return df


def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df


def _strip_column(df, column_id):
    
    df[column_id] = df[column_id].str.strip()

    return df


def _generate_rows_uids(df):
    logger.info('Generating unique ids for each row')
    uids = df.apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis = 1).apply(lambda hash_object: hash_object.hexdigest())

    df['uid'] = uids

    return df.set_index('uid')


def _tokenize_column(df, column_id):
    return (df
              .dropna()
              .apply(lambda row: nltk.word_tokenize(row[column_id]), axis = 1)
              .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
              .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
              .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
              .apply(lambda valid_words: len(valid_words))
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type= str)

    args = parser.parse_args()

    df = main(args.filename)
    print(df)