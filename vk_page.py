from selenium.webdriver.common.by import By
from browser import Browser

AUDIO_LIST_BLOCK = (By.CSS_SELECTOR, '.audio_page__audio_list_block')
SONG_PERFORMER = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__performers a')
SONG_NAME = (By.CSS_SELECTOR, '.audio_page__audio_list_block .audio_row__title._audio_row__title a')
SONG_BLOCK = (By.CSS_SELECTOR, '.audio_row__inner')


class VkPage:

    def __init__(self, driver):
        self.driver = driver

    def should_be_audio_list_block(self):
        assert self.driver.is_element_present(*AUDIO_LIST_BLOCK), 'Ссылка не содержит плейлист'

    def get_song_block(self):
        song_blocks = self.driver.find_elements_is_present(*SONG_BLOCK)
        return song_blocks

    def check_music_page(self):
        self.should_be_audio_list_block()

    def create_music_list_from_vk_music_page(self):
        song_block = self.get_song_block()
        song_list_for_file = []

        for block in song_block:
            parts = block.text.split('\n')
            group_name = parts[0]
            song_name = parts[1]
            song_list_for_file.append(f'{song_name} - {group_name}\n')
        with open('vk_playlist.txt', 'w', encoding='utf-8') as file:
            file.writelines(song_list_for_file)
            print('Плейлист добавлен в файл vk_playlist.txt')

    def scroll_audio_block_vk_page_to_bottom(self):
        self.driver.scroll_element_to_bottom()
