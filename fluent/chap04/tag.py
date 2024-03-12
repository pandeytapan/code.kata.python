def tag(tag_name, *tag_content, cls=None, **attrs) -> str:
    '''
    Generates an HTML tag
    @param tag: The name of the tag
    @param *tag_content: Positional arguments  captured as tuple
    @param cls: Argument that can only be passed as a keyword only argument.
    @param **attrs: All keyword only arguments.
    @return: string formation of the tag
    '''

    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attrs_str = "".join("%s=%s" % (attr, value) for attr, value in
                            sorted(attrs.items()))
    else:
        attrs_str = ''

    if tag_content:
        return '\n'.join("<%s%s>%s</%s>" % (tag_name, attrs_str, c, tag_name) for c in
                         tag_content)
    else:
        return '<%s%s />' % (tag_name, attrs_str)
