import importlib
import logging
import re
import typing

from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse
from markdown_deux import markdown


register = template.Library()


@register.filter
def cross_reference(value: str) -> str:
    """
    Takes a markdown textfield and searches for internal links in the format:

    {{location:phandalin-miners-exchange}}

    where "location" is the designation for a model
    and 'phandalin-miners-exchange' is the slug for a given object.

    NOTE: Must be processed before markdown.

    If it is inside a markdown link, it will resolve with the link text as intended:

    [Miner's Exchange]({{location:phandalin-miners-exchange}})
    [Miner's Exchange](/campaign/location/phandalin-miners-exchange)

    If it is by itself, it will resolve to a linked name:

    {{location:phandalin-miners-exchange}}
    [Phandalin Miner's Exchange](/campaign/location/phandalin-miners-exchange)
    """
    # Pattern(s) inside markdown links first.
    # e.g. [link text]({{location:phandalin}})
    markdown_reference_pattern = r'\[.+\]\({{\S+:\S+}}\)'
    p = re.compile(markdown_reference_pattern)
    processed_text = p.sub(convert_markdown_reference, value)

    # After we replace those, find standalone pattern(s).
    # e.g. {{location:phandalin}}
    standalone_reference_pattern = r'{{\S+:\S+}}'
    p = re.compile(standalone_reference_pattern)

    # replace the captured pattern(s) with the new markdown link(s)
    return p.sub(convert_standalone_reference, processed_text)


def reference_to_dict(string: str) -> dict:
    """
    Takes a local URL pattern and converts it into a link name/url.
    e.g. "{{location:phandalin}}" becomes
    {
        'name': 'Phandalin',
        'url': '/campaign/location/phandalin'
    }
    """
    # Strip off the {{ and }}
    string = string[2:-2]

    # Separate the link type and the slug
    link_type, link_slug = string.split(":")

    # Figure out what view we need to display for the link_type
    link_view = 'campaign:{}_detail'.format(link_type)

    models = importlib.import_module('campaign.models')
    link_model = (getattr(models, link_type.title()))

    entity = get_object_or_404(link_model, slug=link_slug)

    if hasattr(entity, 'campaign'):
        link_url = reverse(link_view, args=(entity.campaign.slug, link_slug))
    else:
        link_url = reverse(link_view, args=[link_slug])

    link_name = entity.name

    # Return name and link_url as a dictionary
    link_dict = {'name': link_name, 'url': link_url}
    return link_dict


def convert_standalone_reference(match: typing.Match) -> str:
    """
    Takes a match object of a standlone reference and converts it into a Markdown link.
    e.g. {{location:phandalin}} -> [Phandalin](/campaign/location/phandalin)
    """
    string = match.group()

    try:
        link_dict = reference_to_dict(string)

        markdown_link = '[{0}]({1})'.format(
            link_dict['name'], link_dict['url']
        )

        return markdown_link
    except Exception:
        logging.exception("Error creating markdown link")

        # Lookup failed, just return original string
        return string


def convert_markdown_reference(match: typing.Match) -> str:
    """
    Takes a match object of a Markdown-formatted reference and expands the relative link.
    e.g. [Phan-da-lin]({{location:phandalin}}) -> [Phan-da-lin](/campaign/location/phandalin)
    """
    string = match.group()

    try:
        # Grab the link text and link pattern
        p_obj = re.search(r'\[(.+)\]\(({{\S+:\S+}})\)', string)
        link_dict = reference_to_dict(p_obj.group(2))

        markdown_link = '[{0}]({1})'.format(
            p_obj.group(1), link_dict['url']
        )

        return markdown_link
    except Exception:
        logging.exception("Error creating markdown link")

        # Lookup failed, just return original string
        return string


def markdownify(content):
    """
    Trans-compiles Markdown text to HTML.
    :param content: Markdown text.
    :type content: str
    :return: HTML encoded text.
    :rtype: str
    """

    cross_referenced = cross_reference(content)

    md = markdown(
        text=cross_referenced,
    )

    html = "{0}".format(md)

    return html
