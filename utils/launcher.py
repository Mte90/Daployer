import glob
import os


class Launcher():

    page = 0
    scripts = []

    def __init__(self):
        self.scripts = self.get_scripts()

    def get_page(self, page):
        page = page * 3
        write = self.scripts[:page]
        write.insert(0, 'Write script number:')
        print('   Printed page ' + str(self.page))
        return write

    def next_page(self):
        self.page = self.page + 1
        self.get_page(self.page)
        pass

    def get_scripts(self):
        items = glob.glob("./scripts/*.sh") + glob.glob("./scripts/*.py")
        if len(items) != 0:
            print_items = []
            for i, x in enumerate(items):
                print_items.append(str(i) + ' ' + os.path.basename(x))
            return print_items
        else:
            return ['No scripts available', '', ':-(']
