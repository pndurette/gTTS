# -*- coding: utf-8 -*-
import sys, os
from utils import send_to_github_env, send_to_github_output

# This script:
# * Compares the current set of languages
#   to one generated from the Internet
# * Generates a commit message for these changes (if any)
#   to the GitHub Actions environment's $LANGS_COMMIT_MESSAGE env var
# * Sets the GitHub Actions step output 'must_commit' to 'true'
#   if a commit is needed, 'false' otherwise

# Pre-requisites:
# * Generate a fresh copy of the languages list from the Internet
#   to the same directory as the current script:
#   `python scripts/gen_langs.py scripts/lang_temps.py`

try:
    # Import languages from the installed gTTS and from lang_temps.py
    # They will be compared for differences
    from gtts.langs import _langs as _current_langs
    from langs_temp import _langs as _new_langs
except ImportError as e:
    print("::error::This script expects the generated 'lang_temps.py' in the same dir")
    sys.exit(1)

added_dict = {}
removed_dict = {}
modified_dict = {}

added = False
removed = False
modified = False
must_commit = False

# Get added languages
for key in _new_langs.keys():
    if not key in _current_langs:
        added_dict[key] = _new_langs[key]
        added = True

# Get removed languages
for key in _current_langs.keys():
    if not key in _new_langs:
        removed_dict[key] = _current_langs[key]
        removed = True

# Get modified languages
# i.e. same key, new value
for key in _new_langs.keys():
    try:
        if _new_langs[key] != _current_langs[key]:
            modified_dict[key] = _new_langs[key]
            modified = True
    except KeyError:
        pass

# Determine is commit is necessary
must_commit = added or removed or modified

# Status
# Using GitHub 'notice' workflow command
print(f"::notice::{added_dict=}")
print(f"::notice::{removed_dict=}")
print(f"::notice::{modified_dict=}")
print(f"::notice::{must_commit=}")

if not must_commit:
    # Nothing to do.
    # Set 'must_commit' output to 'false' and notify
    send_to_github_output("must_commit", "false")
    print(f"::notice::No commit to do")
    sys.exit(0)
else:
    # Set 'must_commit' output to 'true' and notify
    send_to_github_output("must_commit", "true")
    print(f"::notice::Must commit")

# Generate human-readable lists in Markdown
added_markdown = ", ".join([f"`{k}` ({v})" for k, v in added_dict.items()])
removed_markdown = ", ".join([f"`{k}` ({v})" for k, v in removed_dict.items()])
modified_markdown = ", ".join([f"`{k}` ({v})" for k, v in modified_dict.items()])

# Generate commit message
if modified and not added and not removed:
    # Only the language values were modified, can be a 'chore' commit type
    # (which won't trigger a new release)
    commit_message = f"chore(langs): language{'s' if len(modified_dict) > 1 else ''} modified: {modified_markdown}"
else:
    messages = []
    if added:
        messages.append(
            f"language{'s' if len(added_dict) > 1 else ''} added: {added_markdown}"
        )
    if removed:
        messages.append(
            f"language{'s' if len(removed_dict) > 1 else ''} removed: {removed_markdown}"
        )
    if modified:
        messages.append(
            f"language{'s' if len(modified_dict) > 1 else ''} modified: {modified_markdown}"
        )

    commit_message = "fix(langs): " + "; ".join(messages)

# Set LANGS_COMMIT_MESSAGE env var to commit message
print(f"::notice::{commit_message=}")
send_to_github_env("LANGS_COMMIT_MESSAGE", commit_message)
