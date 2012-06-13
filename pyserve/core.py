from datetime import datetime
from os import path as op, listdir

from .icons import ICONS_BY_EXT, ICONS_BY_NAME


def compare(e):
    return "%s%s" % (isinstance(e, File), e.name)


class Entry(object):

    default_icon = 'cross.png'
    hidden = True

    def __init__(self, path, root=None):
        self.root = root
        self.path = path
        self.abspath = root.join(path)
        self.name = op.basename(self.abspath)
        self.hidden = self.name.startswith('.')

    def __new__(self, path, root=None):
        if not root or not path or path == '/':
            return RootDirectory.__new__(RootDirectory, path)

        else:

            abspath = root.join(path)
            if op.isdir(abspath):
                return Directory.__new__(Directory, path, root)

            elif op.isfile(abspath):
                return File.__new__(File, path, root)

            else:
                raise IOError('{0} does not exists.'.format(abspath))

    def join(self, path):
        path = path.strip('/')
        return op.join(self.abspath, path) if path else self.abspath

    def parse(self, path):
        abspath = op.abspath(self.join(path))
        if self.abspath == abspath:
            return self
        return Entry(path, root=self)

    @staticmethod
    def is_file():
        return False

    @property
    def link(self):
        if not self.path.startswith('/'):
            return "/" + self.path
        return self.path

    @property
    def icon(self):
        return self.default_icon

    @property
    def modified(self):
        return datetime.fromtimestamp(op.getmtime(self.abspath))

    @property
    def size(self):
        return op.getsize(self.abspath)

    def __str__(self):
        return "<%s [%s]>" % (self.__class__.__name__, self.abspath)

    __repr__ = __str__


class Directory(Entry):
    default_icon = 'folder.png'

    def __new__(self, *args, **kwargs):
        return object.__new__(Directory, *args, **kwargs)

    @property
    def breadcrumb(self):
        paths = [''] + self.abspath[len(self.root.abspath):].split('/')
        paths.pop()
        breadcrumb = []
        while paths:
            path = op.join(*paths)
            paths.pop()
            breadcrumb.append(Entry(path, root=self.root))
        return reversed(list(enumerate(breadcrumb)))

    def is_root(self):
        return self == self.root

    @property
    def entries(self):
        entries = []

        for path in listdir(self.abspath):
            if self.hidden or not path.startswith('.'):
                entries.append(Entry(op.join(self.path, path), self.root))
        entries.sort(key=compare)

        if not self.is_root():
            entries.insert(0, ParentDirectory(self.path, self.root))

        return entries


class File(Entry):
    default_icon = 'file.png'

    def __new__(self, *args, **kwargs):
        return object.__new__(File, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.ext = op.splitext(self.name)[1].strip('.')

    @staticmethod
    def is_file():
        return True

    @property
    def icon(self):
        return ICONS_BY_NAME.get(
                    self.name,
                    ICONS_BY_EXT.get(
                        self.ext,
                        self.default_icon
                    ))


class RootDirectory(Directory):
    default_icon = 'root.png'

    def __init__(self, path, root=None):
        self.abspath = op.abspath(path)
        super(RootDirectory, self).__init__('/', self)
        self.name = 'root'

    def __new__(self, *args, **kwargs):
        return object.__new__(RootDirectory, *args, **kwargs)

    @property
    def breadcrumb(self):
        return []

    @property
    def link(self):
        return self.path


class ParentDirectory(Directory):
    default_icon = 'parent.png'

    def __init__(self, path, root=None):
        path = op.dirname(path)
        super(ParentDirectory, self).__init__(path, root=root)
        self.name = '..'

    def __new__(self, *args, **kwargs):
        return object.__new__(ParentDirectory, *args, **kwargs)
