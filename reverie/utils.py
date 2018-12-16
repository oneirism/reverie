from markdown_deux import markdown


def markdownify(content):
    """
    Trans-compiles Markdown text to HTML.
    :param content: Markdown text.
    :type content: str
    :return: HTML encoded text.
    :rtype: str
    """

    md = markdown(
        text=content,
    )

    html = "{0}".format(md)

    return html
