
from pathlib import Path
from typing import Iterable
from os.path import isdir
home = Path.home()

from textual.app import App, ComposeResult
from textual.widgets import Header, DirectoryTree, Static, Button, Input, RichLog
from textual.containers import Horizontal, Vertical, VerticalScroll, Container

from os import system, listdir

def move(file, path):
    system(f'move {file} {path}')	

def move_with_extension(folder, extension):
    for file in listdir(folder):
        if file.endswith(extension):
            move(file, folder)

class DirectoryWidget(Vertical):
    def __init__(self, dir=str(home), **kwargs):
        super().__init__(**kwargs)
        self.classes='dirwidget'
        self.directory = Static(dir, classes='dirwidget-directory')
        self.extensions = Input(placeholder='File extensions (commas, no spaces)', classes='dirwidget-extensions')
    def compose(self) -> ComposeResult: 
        yield self.directory
        yield self.extensions

class FolderDirectoryTree(DirectoryTree):
    def __init__(self, path: Path, **kwargs):
        super().__init__(path, **kwargs)
        self.path = path
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if isdir(path)]

class RightPanel(Vertical):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classes='side-panel'
        self.dirs = VerticalScroll(id='dirs-container')
    def compose(self) -> ComposeResult:
        yield Button(label='Add selected directory', id='add-dir-button')
        yield self.dirs

class FolderOrganizer(App):
    CSS_PATH='style.tcss'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_path = str(home)
        self.inp_texts = {}
    def compose(self) -> ComposeResult:
        yield Header()

        self.dirtree = FolderDirectoryTree(home, id='main-tree')
        self.left_panel = Vertical(
            Button(label='Organize selected folder', id='organize-button'),
            RichLog(id='log'),
            id='left-panel', classes='side-panel'
        )
        self.right_panel = RightPanel()

        yield Horizontal(
            self.left_panel,
            self.dirtree,
            self.right_panel
        )
    
    def on_input_changed(self, event: Input.Changed) -> None:
        self.inp_texts[event.input.id] = event.value

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'add-dir-button':
            self.right_panel.dirs.mount(
                DirectoryWidget(dir=str(self.current_path))
            )
        if event.button.id == 'organize-button':
            for dirwidget in self.right_panel.dirs.query(DirectoryWidget):
                for ext in self.inp_texts[dirwidget.id].split(', '):
                    move_with_extension(dirwidget.directory._content, ext)

    def on_directory_tree_directory_selected(self, event: DirectoryTree.DirectorySelected) -> None:
        self.current_path = event.path

if __name__ == '__main__':
    FolderOrganizer().run()