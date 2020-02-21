from collections import OrderedDict
from datetime import datetime
import os, io

MARKDOWN_ARCHIVE="output/markdown"
JEKYLL_BUNDLE="output/jekyll"
RESOURCE_DIR="{}/resources".format(JEKYLL_BUNDLE)


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

class JekyllPage:
    content = ""

    frontMatters = OrderedDict()
    body = ""
    create_date = None


    def __init__(self, path):
        print('read file from: {}'.format(path))
        self.create_date = datetime.fromtimestamp(os.path.getctime(path))
        with open(path) as f:
            self.content = f.read()
        # parse data from the file
        self.parse()
    
    def output(self, path):
        print("saving files to {}...".format(path))

        ensure_dir(os.path.dirname(path))
        with open(path, 'w') as f:
            # write front matters
            f.write('---\n')
            for name, text in self.frontMatters.items():
                f.write(" {}: {}\n".format(name, text))
            f.write('---\n')

            # write body
            f.write(self.body)


    def parse(self):
        # parse front matters and body
        self.parse_structure(self.content)

        # parse resources
        self.parse_resources(self.body)

    def parse_date(self,datestr):
        try:
            return datetime.strptime(datestr, "%Y-%m-%d %H:%M")
        except ValueError:
            try:
                return datetime.strptime(datestr, "%Y-%m-%d")
            except ValueError:
                return None

    def parse_structure(self, content):
        reader = io.StringIO(content)
        line = reader.readline()
        is_in_front_matter = False
        while line:
            if is_in_front_matter and line.find("---") != 0:
                colon_index = line.find(":")
                name = line[:colon_index].strip()
                text = line[colon_index+1:].strip()
                self.frontMatters[name] = text

            if line.rstrip().find('---') >= 0 or line.rstrip().find('===') >= 0:
                is_in_front_matter = not is_in_front_matter
                if not is_in_front_matter:
                    self.body = reader.read() # rest content are body
                    break

            # next line
            line = reader.readline()
            

        if self.frontMatters.get("date"):
            publish_date = self.parse_date(self.frontMatters["date"])
            if publish_date:
                self.create_date = publish_date

    def parse_resources(self, body):
        pass


    def get_file_name(self):
        title = self.frontMatters.get("title", "")
        create_date = self.create_date
        return "{}-{}.md".format(create_date.strftime("%Y-%m-%d"), title)



def main():
    for root, dirs, files in os.walk(MARKDOWN_ARCHIVE):
        for fname in files:
            if fname.rfind('.md') != -1:
                source_file = os.path.join(root, fname)
                page = JekyllPage(source_file)
                
                output_file = os.path.join(JEKYLL_BUNDLE, page.get_file_name())
                page.output(output_file)


if __name__ == "__main__":
    main()

