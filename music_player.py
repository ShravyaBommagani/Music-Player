import os
import pygame
from tkinter import Tk, Label, Button, Listbox, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        self.playlist = Listbox(master, selectmode="SINGLE", bg="lightgray", selectbackground="darkblue", selectforeground="white")
        self.playlist.pack(pady=20)

        self.load_button = Button(master, text="Load Music", command=self.load_music)
        self.load_button.pack()

        self.play_button = Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.current_track_label = Label(master, text="Current Track: ")
        self.current_track_label.pack()

        self.music_folder = ""
        self.music_list = []
        self.current_track = 0

        self.mixer_initialized = False

    def load_music(self):
        self.music_folder = filedialog.askdirectory()
        if self.music_folder:
            self.music_list = [f for f in os.listdir(self.music_folder) if f.endswith((".mp3", ".wav"))]
            self.playlist.delete(0, "end")
            for track in self.music_list:
                self.playlist.insert("end", track)

    def play_music(self):
        if not self.mixer_initialized:
            pygame.mixer.init()
            self.mixer_initialized = True

        if self.music_list:
            selected_track = self.playlist.curselection()
            if selected_track:
                self.current_track = selected_track[0]
                track_path = os.path.join(self.music_folder, self.music_list[self.current_track])
                pygame.mixer.music.load(track_path)
                pygame.mixer.music.play()
                self.current_track_label.config(text=f"Current Track: {self.music_list[self.current_track]}")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track_label.config(text="Current Track: ")

if __name__ == "__main__":
    root = Tk()
    player = MusicPlayer(root)
    root.mainloop()


