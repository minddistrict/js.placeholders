from fanstatic import Library, Resource

library = Library('placeholders.js', 'resources')

placeholders = Resource(
    library, 'placeholders.js', minified='placeholders.min.js')
