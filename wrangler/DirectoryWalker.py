import os

# Takes a directory and transforms the matching elements into the matching class.
class DirectoryWalker():
    def __init__(self, params):
        self.item_class = params['item_class']
        self.input_dir = params['input_dir']
        self.ignore_files = params['ignore_files']
        self.valid_extensions = params['valid_extensions']

    def fetch(self):
        items = []
        # Walk the input directory and ignore hidden files, partials
        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                # Ignore hidden files etc
                if any(file.startswith(x) for x in self.ignore_files):
                   continue;
                # Process valid extensions
                if any(file.endswith(x) for x in self.valid_extensions):
                    item = self.item_class(file, self.input_dir, root)
                    items.append(item)
        return items