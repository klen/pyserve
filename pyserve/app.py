" Define web application. "

from .bottle import static_file, Bottle, template, HTTPError


APP = Bottle()


@APP.route('/__serve_static__/<path:re:.*>')
def static(path):
    return static_file(path, APP.config.static)


@APP.route('/')
@APP.route('/<path:re:.*>')
def index(path=''):
    try:
        entry = APP.config.root.parse(path)
        entry.hidden = APP.config.hidden

        if entry.is_file():
            return static_file(path, APP.config.root.abspath)

        if APP.config.autoindex:
            index = [e for e in entry.entries if e.name in ['index.html', 'index.htm']]
            if index:
                return static_file(index[0].path, APP.config.root.abspath)

        return template('_pyserve_.html',
                template_lookup=[APP.config.static],
                dir=entry,
                app=APP)

    except IOError:
        return HTTPError(404)
