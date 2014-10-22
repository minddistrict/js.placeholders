from fanstatic import Library, Resource
from fanstatic.core import render_js


def ie_lte9_conditional_inclusion(url):
    return '''<!--[if lte IE 9]>{}<![endif]-->'''.format(render_js(url))


library = Library('placeholders.js', 'resources')

placeholders = Resource(
    library, 'placeholders.js', minified='placeholders.min.js',
    renderer=ie_lte9_conditional_inclusion)
