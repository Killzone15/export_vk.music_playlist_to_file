import tkinter as tk
from tkinter import messagebox
from browser import Browser
from vk_page import VkPage


class VKMusicExporter:

    def __init__(self, root):
        self.root = root
        self.root.title("Экспорт музыки из VK")

        self.label = tk.Label(root, text="Введите ссылку на страницу VK:")
        self.label.pack()

        self.link_entry = tk.Entry(root)
        self.link_entry.pack()

        self.export_button = tk.Button(root, text="Экспорт в файл txt", command=self.export_music)
        self.export_button.pack()

    def export_music(self):
        # Получите ссылку из поля ввода
        vk_link = self.link_entry.get()

        # Откройте VK и выполните необходимые действия
        driver = Browser(vk_link)
        driver.open()

        page = VkPage(driver)
        page.check_music_page()
        page.scroll_audio_block_vk_page_to_bottom()
        page.create_music_list_from_vk_music_page()

        messagebox.showinfo("Готово", "Музыка была успешно экспортирована в файл vk_playlist.txt")


def create_window():
    root = tk.Tk()
    VKMusicExporter(root)
    root.mainloop()
