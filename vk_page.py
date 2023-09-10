from selenium.webdriver.common.by import By
from browser import Browser

AUDIO_LIST_BLOCK = (By.CSS_SELECTOR, '.audio_page__audio_list_block')
SONG_PERFORMER = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__performers a')
SONG_NAME = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__title._audio_row__title a')
SONG_BLOCK = (By.CSS_SELECTOR, '.audio_row__inner')


class VkPage:
    @staticmethod
    def should_be_audio_list_block(driver):
        assert driver.is_element_present(*AUDIO_LIST_BLOCK), 'Ссылка не содержит плейлист'

    @staticmethod
    def get_song_block(driver):
        song_blocks = driver.find_elements_is_present(*SONG_BLOCK)
        return song_blocks
