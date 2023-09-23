import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
from browser import Browser
from vk_page import VkPage


class VKMusicExporter:

    def __init__(self, root):
        self.root = root
        self.root.title("Экспорт музыки из VK в файл txt")

        self.label = tk.Label(root, text="Введите ссылку на плейлист VK:", bg='#424242',
                              font=("Trebuchet Ms", 15, 'bold'),
                              fg='#e1e3e6')
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.link_entry = tk.Entry(root, width=50)
        self.link_entry.grid(row=1, column=0, padx=10, pady=10, sticky='new')

        self.export_button = tk.Button(root, text="Экспорт в файл txt", command=self.export_music, pady=8)
        self.export_button.grid(row=2, column=0, padx=10, pady=15, sticky='s')

        # Создаем прогресс-бар и размещаем его в новой строке (row=3)
        self.progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate')
        self.progress_bar.grid(row=3, column=0, sticky='nsew', columnspan=2)

        self.root.grid_columnconfigure(0, weight=1)  # Разрешаем растягивание столбца
        self.root.grid_rowconfigure(1, weight=1)  # Разрешаем растягивание строки с полем ввода

        self.root.minsize(650, 500)
        self.root.configure(bg="#424242")

    def export_music(self):
        # Получите ссылку из поля ввода
        vk_link = self.link_entry.get()

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
