import curses
import sys

# [buffer]
class Buffer:
    def __init__(self, lines):
        assert isinstance(lines, list)
        assert all(isinstance(s, str) for s in lines)
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]
# [/buffer]

    # [bottom]
    def bottom(self):
        return len(self.lines) - 1
    # [/bottom]

class Window:
    def __init__(self, nrow, ncol):
        assert 0 <= nrow and 0 <= ncol
        self.nrow = nrow
        self.ncol = ncol
        self.row = 0

    def bottom(self):
        return self.row + self.nrow - 1

    def up(self, cur):
        if (cur.row == self.row - 1) and (self.row > 0):
            self.row -= 1

    # [down]
    def down(self, buf, cur):
        if (cur.row == self.bottom() + 1) and (self.bottom() < buf.bottom()):
            self.row += 1
    # [/down]

    def translate(self, cur):
        return cur.row - self.row, cur.col

class Cursor:
    def __init__(self, row, col):
        assert 0 <= row and 0 <= col
        self.row = row
        self.col = col

class Editor:
    def __init__(self):
        self.scr = None
        self.win = None
        self.cur = None
        self.running = True
        self.actions = {
            "Q": self.quit,
            "q": self.quit,
            "KEY_UP": self.up,
            "KEY_DOWN": self.down,
            "KEY_LEFT": self.left,
            "KEY_RIGHT": self.right
        }

    def __call__(self, scr, buf):
        self.setup(scr, buf)
        self.interact()

    # [setup]
    def setup(self, scr, buf):
        self.scr = scr
        self.buf = buf
        self.win = Window(curses.LINES - 1, curses.COLS - 1)
        self.cur = Cursor(0, 0)
    # [/setup]

    def interact(self):
        while self.running:
            self.display()
            key = self.scr.getkey()
            if key in self.actions:
                self.actions[key]()

    def display(self):
        self.scr.erase()
        visible = self.buf[self.win.row : (self.win.row + self.win.nrow)]
        for i, line in enumerate(visible):
            self.scr.addstr(i, 0, line[:self.win.ncol])
        self.scr.move(*self.win.translate(self.cur))

    def quit(self):
        self.running = False

    def left(self):
        if self.cur.col > 0:
            self.cur.col -= 1
        self.win.up(self.cur)

    def right(self):
        line_len = len(self.buf[self.cur.row])
        if self.cur.col < min(self.win.ncol - 1, line_len - 1):
            self.cur.col += 1
        self.win.down(self.buf, self.cur)

    def up(self):
        if self.cur.row > 0:
            self.cur.row -= 1
        self.limit_col()
        self.win.up(self.cur)

    def down(self):
        if self.cur.row < len(self.buf) - 1:
            self.cur.row += 1
        self.limit_col()
        self.win.down(self.buf, self.cur)

    def limit_col(self):
        self.cur.col = min(self.cur.col, len(self.buf[self.cur.row]) - 1)

def make_buffer():
    line = '0123456789'
    result = []
    for i in range(10):
        result.append(f"{i:3}:{line[:i+1]}")
    return Buffer(result)

if __name__ == "__main__":
    editor = Editor()
    buf = make_buffer()
    try:
        curses.wrapper(editor, buf)
    except Exception as exc:
        print(exc)
