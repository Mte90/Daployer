import glob
import os


class Launcher():

    page = 1
    scripts = []

    def __init__(self):
        self.scripts = self.get_scripts()

    def run(self, number):
        if number in self.scripts:
            return True, ['', 'Script executed:', self.scripts[number], '']
        else:
            return False, ['', 'Script not found', 'Try again', '']

    def get_page(self, page):
        page = page * 3
        previous_page = page - 3
        if page == 1:
            write = self.scripts[:page]
        else:
            write = self.scripts[previous_page:page]

        write.insert(0, 'Write script number:')
        print('   Printed page ' + str(self.page))
        return write

    def next_page(self):
        if (self.page * 3) < len(self.scripts):
            self.page = self.page + 1
            return self.get_page(self.page)
        else:
            return False

    def previous_page(self):
        if self.page != 1:
            self.page = self.page - 1
            return self.get_page(self.page)
        else:
            return False

    def get_scripts(self):
        items = glob.glob("./scripts/*.sh") + glob.glob("./scripts/*.py")
        if len(items) != 0:
            print_items = []
            for i, x in enumerate(items):
                print_items.append(str(i) + ') ' + os.path.basename(x))
            return print_items
        else:
            return ['No scripts available', '', ':-(']
