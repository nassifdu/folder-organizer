
from pathlib import Path
home = Path.home()

from textual.app import App, ComposeResult
from textual.widgets import Label, DirectoryTree
from textual.containers import Horizontal, Vertical

class FolderOrganizer(App):
    CSS_PATH='style.tcss'
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(id='left-panel'),
            DirectoryTree(home, id='main-tree'),
            Vertical(id='right-panel')
        )

if __name__ == '__main__':
    FolderOrganizer().run()