from selenium.webdriver.common.by import By


from browser import Browser

AUDIO_LIST_BLOCK = (By.CSS_SELECTOR, '.audio_page__audio_list_block')


class VkPage():

    def should_be_audio_list_block(self, driver):
        assert driver.is_element_present(*AUDIO_LIST_BLOCK), 'Ссылка не содержит плейлист'
