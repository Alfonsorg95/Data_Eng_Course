import logging
import subprocess
from extract.common import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
news_sites_uids = list(config('extract/')['news_sites'].keys())


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python3', 'main.py', news_site_uid], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid),
                         '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid),
                          ';'], cwd='./extract')


def _transform():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_file = '{}_.csv'.format(news_site_uid)
        clean_data_file = 'clean_{}'.format(dirty_data_file)
        subprocess.run(['python3', 'main.py', dirty_data_file], cwd='./transform')
        subprocess.run(['rm', dirty_data_file], cwd='./transform')
        subprocess.run(['mv', clean_data_file, '../load/{}.csv'.format(news_site_uid)], cwd='./transform')     


def _load():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        clean_data_file = '{}.csv'.format(news_site_uid)
        subprocess.run(['python3', 'main.py', clean_data_file], cwd='./load')
        subprocess.run(['rm', clean_data_file], cwd='./load')


if __name__ == '__main__':
    main()