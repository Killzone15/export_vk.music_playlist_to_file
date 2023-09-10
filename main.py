from browser import Browser
from vk_page import VkPage


def open_vk():
    driver = Browser('https://vk.com/audios93781810')
    driver.open()
    return driver


def check_music_page(driver):
    page = VkPage()
    page.should_be_audio_list_block(driver)


def create_music_list_from_vk_music_page(driver):
    page = VkPage()
    song_block = page.get_song_block(driver)
    song_list_for_file = []

    for block in song_block:
        parts = block.text.split('\n')
        group_name = parts[0]
        song_name = parts[1]
        song_list_for_file.append(f'{song_name} - {group_name}\n')
    with open('vk_playlist.txt', 'w', encoding='utf-8') as file:
        file.writelines(song_list_for_file)
        print('Плейлист добавлен в файл vk_playlist.txt')


def scroll_audio_block_vk_page_to_bottom():
    driver.scroll_element_to_bottom()


if __name__ == '__main__':
    driver = open_vk()
    check_music_page(driver)
    scroll_audio_block_vk_page_to_bottom()
    create_music_list_from_vk_music_page(driver)
