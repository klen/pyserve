" Define web application. "

import bottle


APP = bottle.Bottle()


@APP.route('/__serve_static__/<path:re:.*>')
def static(path):
    return bottle.static_file(path, APP.config.static)


@APP.route('/')
@APP.route('/<path:re:.*>')
def index(path=''):
    try:
        entry = APP.config.root.parse(path)

        if entry.is_file():
            return bottle.static_file(path, APP.config.root.abspath)

        if APP.config.autoindex:
            index = [e for e in entry.entries if e.name in ['index.html', 'index.htm']]
            if index:
                return bottle.static_file(index[0].path, APP.config.root.abspath)

        return bottle.template('_pyserve_.html',
                template_lookup=[APP.config.static],
                dir=entry,
                app=APP)

    except IOError, e:
        return e
        bottle.redirect('/')
