# -*- coding: utf-8 -*-

from transliterate.base import TranslitLanguagePack, registry
from transliterate.contrib.languages.ar import data

__title__ = 'transliterate.contrib.languages.ar.translit_language_pack'
__author__ = 'Omar Shaban'
__copyright__ = '2020 Omar Shaban'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('ArabicLanguagePack',)


class ArabicLanguagePack(TranslitLanguagePack):
    """Language pack for Arabic language.

    See `https://en.wikipedia.org/wiki/Arabic_alphabet` for
    details.
    """
    language_code = "ar"
    language_name = "Arabic"
    character_ranges = ((0x0400, 0x04FF), (0x0500, 0x052F))
    mapping = data.mapping
    reversed_specific_mapping = data.reversed_specific_mapping
    pre_processor_mapping = data.pre_processor_mapping
    detectable = True


registry.register(ArabicLanguagePack)
