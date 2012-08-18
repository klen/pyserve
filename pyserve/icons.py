by_ext = [
    ('py.png', 'py'),
    ('python.png', 'pyc'),
    ('page_white_text_width.png', ['md', 'markdown', 'rst', 'rtf']),
    ('page_white_text.png', 'txt'),
    ('page_white_code.png', ['html', 'htm', 'cgi']),
    ('page_white_visualstudio.png', ['asp', 'vb']),
    ('page_white_ruby.png', 'rb'),
    ('page_code.png', 'xhtml'),
    ('page_white_code_red.png', ['xml', 'xsl', 'xslt', 'yml']),
    ('script.png', ['js', 'json', 'applescript', 'htc']),
    ('layout.png', ['css', 'less']),
    ('page_white_php.png', 'php'),
    ('page_white_c.png', 'c'),
    ('page_white_cplusplus.png', 'cpp'),
    ('page_white_h.png', 'h'),
    ('database.png', ['db', 'sqlite', 'sqlite3']),
    ('page_white_database.png', 'sql'),
    ('page_white_gear.png', ['conf', 'cfg', 'ini', 'reg', 'sys']),
    ('page_white_zip.png', ['zip', 'tar', 'gz', 'tgz', '7z', 'alz', 'rar',
                            'bin', 'cab']),
    ('cup.png', 'jar'),
    ('page_white_cup.png', ['java', 'jsp']),
    ('application_osx_terminal.png', 'sh'),
    ('page_white_acrobat.png', 'pdf'),
    ('package.png', ['pkg', 'dmg']),
    ('shape_group.png', ['ai', 'svg', 'eps']),
    ('application_osx.png', 'app'),
    ('cursor.png', 'cur'),
    ('feed.png', 'rss'),
    ('cd.png', ['iso', 'vcd', 'toast']),
    ('page_white_powerpoint.png', ['ppt', 'pptx']),
    ('page_white_excel.png', ['xls', 'xlsx', 'csv']),
    ('page_white_word.png', ['doc', 'docx']),
    ('page_white_flash.png', 'swf'),
    ('page_white_actionscript.png', ['fla', 'as']),
    ('comment.png', 'smi'),
    ('disk.png', ['bak', 'bup']),
    ('application_xp_terminal.png', ['bat', 'com']),
    ('application.png', 'exe'),
    ('key.png', 'cer'),
    ('cog.png', ['dll', 'so']),
    ('pictures.png', 'ics'),
    ('picture.png', ['gif', 'png', 'jpg', 'jpeg', 'bmp', 'ico']),
    ('film.png', ['avi', 'mkv']),
    ('error.png', 'log'),
    ('music.png', ['mpa', 'mp3', 'off', 'wav']),
    ('font.png', ['ttf', 'eot']),
    ('vcard.png', 'vcf')
]

ICONS_BY_NAME = dict(
    Makefile='page_white_gear.png',
    Rakefile='page_white_gear.png',
    README='page_white_text_width.png',
    LICENSE='shield.png',

)

ICONS_BY_EXT = dict()
for icon, exts in by_ext:
    if not isinstance(exts, list):
        exts = [exts]
    for e in exts:
        ICONS_BY_EXT[e] = icon
