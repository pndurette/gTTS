# -*- coding: utf-8 -*-

# TODO: Add logging to gen_langs.py (it takes 28 seconds to run!)

# Order of things:
# X Generate new file to temp location
# X Load existing file
# X Load new file
# X Do a diff (?)
# X Get list of added
# X Get list of removed
# If any of the above is not empty:
#   Copy temp file to existing file
#   Create commit to new branch
#   Open PR

# TODO: Expects the output of gen_langs.py into temp.py
from gtts.langs import _langs as _current_langs
from temp import _langs as _new_langs

added_dict = {}
removed_dict = {}
changed_dict = {}

added = False
removed = False
changed = False

for key in _new_langs.keys():
    if not key in _current_langs:
        added_dict[key] = _new_langs[key]
        added = True

for key in _current_langs.keys():
    if not key in _new_langs:
        removed_dict[key] = _current_langs[key]
        removed = True

for key in _new_langs.keys():
    try:
        if _new_langs[key] != _current_langs[key]:
            changed_dict[key] = _new_langs[key]
            changed = True
    except KeyError:
        pass

print(f"{added_dict=}")
print(f"{removed_dict=}")
print(f"{changed_dict=}")

added_markdown = ", ".join([f"`{k}` ({v})" for k,v in added_dict.items()])
removed_markdown = ", ".join([f"`{k}` ({v})" for k,v in removed_dict.items()])
changed_markdown = ", ".join([f"`{k}` ({v})" for k,v in changed_dict.items()])

added_commit = f"fix: Language{'s' if added > 1 else ''} added: {added_markdown}"
removed_commit = f"fix: Language{'s' if removed > 1 else ''} removed: {removed_markdown}"
changed_commit = f"fix: Language{'s' if changed > 1 else ''} changed: {changed_markdown}"

print(f"{added_commit=}")
print(f"{removed_commit=}")
print(f"{changed_commit=}")