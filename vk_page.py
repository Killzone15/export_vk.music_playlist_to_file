from selenium.webdriver.common.by import By
from browser import Browser

AUDIO_LIST_BLOCK = (By.CSS_SELECTOR, '.audio_page__audio_list_block')
SONG_PERFORMER = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__performers a')
SONG_NAME = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__title._audio_row__title a')


class VkPage:
    @staticmethod
    def should_be_audio_list_block(driver):
        assert driver.is_element_present(*AUDIO_LIST_BLOCK), 'Ссылка не содержит плейлист'

    @staticmethod
    def get_song_performer_text(driver):
        song_performer = driver.find_element_is_present(*SONG_PERFORMER)
        song_performer_text = song_performer.text
        return song_performer_text

    @staticmethod
    def get_song_name_text(driver):
        song_name = driver.find_element_is_present(*SONG_NAME)
        song_name_text = song_name.text
        return song_name_text

    @staticmethod
    def get_all_songs_name(driver):
        songs_name_list = driver.find_elements_is_present(*SONG_NAME)
        return songs_name_list

    @staticmethod
    def get_all_songs_performers(driver):
        songs_performers_list = driver.find_elements_is_present(*SONG_PERFORMER)
        return songs_performers_list

    @staticmethod
    def scroll_audio_block_to_bottom(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
