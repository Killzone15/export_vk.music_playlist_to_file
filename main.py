from browser import Browser
from vk_page import VkPage


def open_vk():
    browser = Browser('https://vk.com/audios8554827?section=all')
    browser.open()
    return browser


def check_music_page(browser):
    page = VkPage()
    page.should_be_audio_list_block(browser)


def create_music_list_from_vk_music_page(browser):
    page = VkPage()
    song_name = page.get_all_songs_name(browser)
    song_performer = page.get_all_songs_performers(browser)
    song_list_for_file = []
    for name, performer in zip(song_name, song_performer):
        song_list_for_file.append(f'{name.text} - {performer.text}\n')
    with open('vk_playlist.txt', 'w', encoding='utf-8') as file:
        file.writelines(song_list_for_file)


def scroll_audio_block_vk_page_to_bottom(browser):
    page = VkPage()
    page.scroll_audio_block_to_bottom(browser)


if __name__ == '__main__':
    driver = open_vk()
    check_music_page(driver)
    # scroll_audio_block_vk_page_to_bottom(driver)
    create_music_list_from_vk_music_page(driver)
