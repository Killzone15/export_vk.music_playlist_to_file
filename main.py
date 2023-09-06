from browser import Browser
from vk_page import VkPage


def open_vk():
    browser = Browser('https://vk.com/audios249160567')
    browser.open()
    return browser


def check_music_page(browser):
    page = VkPage()
    page.should_be_audio_list_block(browser)


if __name__ == '__main__':
    driver = open_vk()
    check_music_page(driver)