# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from pelican.contents import Content, is_valid_content
from pelican.generators import Generator
from pelican import signals


logger = logging.getLogger(__name__)


class AuthorBiography(Content):
    """Wrapper class for AuthorBiography content to live in."""
    mandatory_properties = ('slug',)
    default_template = 'page'


class AuthorBiographyManager(object):
    """Manager for easy access to biography objects in templates."""

    def __init__(self):
        self.biographies = {}

    def add(self, biography):
        if not isinstance(biography, AuthorBiography):
            raise Exception(
                "This manager only accepts 'AuthorBiography' objects")

        self.biographies[biography.slug] = biography

    def get(self, slug):
        return self.biographies.get(slug, None)


class AuthorBiographyGenerator(Generator):
    """Pelican generator that:
      - parses author biography files
      - puts those biographys in a AuthorBiographyManager
      - puts the AuthorBiographyManager into global template context

    """

    def __init__(self, *args, **kwargs):
        self.authors_info = AuthorBiographyManager()
        super(AuthorBiographyGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        for author_file in self.get_files(
            self.settings.get('AUTHOR_DIR', 'authors'),
            exclude=self.settings.get('AUTHOR_EXCLUDES', ''),
        ):
            try:
                author = self.readers.read_file(
                    base_path=self.path,
                    path=author_file,
                    content_class=AuthorBiography,
                    context=self.context,
                )
            except Exception as e:
                logger.warning(
                    "Could not process author {0}\n{1}".format(author_file, e))
                continue

            if is_valid_content(author, author_file):
                self.authors_info.add(author)

        self._update_context(('authors_info',))
        self.context['authors_info'] = self.authors_info


def get_generators(generators):
    """Helper function for Pelican to get generator."""
    return AuthorBiographyGenerator


def register():
    """Starting point for Pelican to instantiate plugin."""
    signals.get_generators.connect(get_generators)
