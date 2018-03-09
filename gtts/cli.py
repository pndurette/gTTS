# -*- coding: utf-8 -*-
from gtts import gTTS, gTTSError, Languages, LanguagesFetchError, __version__
import traceback
import click
import sys

# Click settings
CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help']
}


def validate_text(ctx, param, value):
    """Validation callback for the <text> argument.
    Ensures <text> (arg) and <file> (opt) are mutually exclusive
    """
    if not value and 'file' not in ctx.params:
        # No <text> and no <file>
        raise click.BadParameter(
            "TEXT or -f/--file FILENAME required")
    if value and 'file' in ctx.params:
        # Both <text> and <file>
        raise click.BadParameter(
            "TEXT and -f/--file FILENAME can't be used together")
    return value


def print_languages(ctx, param, value):
    """Prints sorted pretty-printed list of supported languages"""
    if not value or ctx.resilient_parsing:
        return
    try:
        langs = Languages().get()
        langs_str_list = sorted("{}: {}".format(k, langs[k]) for k in langs)
        click.echo('  ' + '\n  '.join(langs_str_list))
    except LanguagesFetchError as e:
        # click.echo(str(e), err=True)
        #(_, _, exc_traceback) = sys.exc_info()
        traceback.print_exc()
        raise click.ClickException("Couldn't fetch language list.")
    ctx.exit()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('text', required=False, callback=validate_text)
@click.option(
    '-f',
    '--file',
    type=click.File(),
    help="Input is contents of FILENAME instead of TEXT (use '-' for stdin).")
@click.option(
    '-o',
    '--output',
    type=click.File(mode='wb'),
    help="Write to FILENAME instead of stdout.")
@click.option(
    '-s',
    '--slow',
    default=False,
    is_flag=True,
    help="Read more slowly.")
@click.option(
    '-l',
    '--lang',
    default='en',
    show_default=True,
    help="IETF language tag. Language to speak in. List documented tags with -a/--all.")
@click.option(
    '--nocheck',
    default=False,
    is_flag=True,
    help="Disable strict IETF language tag checking. Allow undocumented tags.")
@click.option(
    '--all',
    default=False,
    is_flag=True,
    callback=print_languages,
    expose_value=False,
    is_eager=True,
    help="Print all documented available IETF language tags and exit.")
@click.option(
    '--debug',
    default=False,
    is_flag=True,
    help="Show debug information.")
@click.version_option(version=__version__)
def tts_cli(text, file, output, slow, lang, nocheck, debug):
    """Reads TEXT to MP3 format using Google Translate's Text-to-Speech API.
    (use '-' as TEXT or as -f/--file FILENAME for stdin)
    """

    # Language check
    # (We can't do callback validation on <lang> because we
    # have to check against <nocheck> which might not exist
    # in the Click context at the time <lang> is used)
    check = not nocheck  # Readability
    if check:
        try:
            if lang.lower() not in Languages().get():
                msg = "Use --all to list languages, or add --nocheck to disable language check."
                raise click.BadParameter(msg, param_hint="lang '{}'".format(lang))
        except LanguagesFetchError as e:
            # We ignore the language check but warn
            click.echo("Warning: %s" % str(e))

    # stdin for <text> (auto for <file>)
    # TODO ValueError (when errors is 'strict')
    # raise click.BadParameter
    if text is '-':
        text = click.get_text_stream('stdin').read()

    # stdout (when no <output>)
    # TODO ValueError (when errors is 'strict')
    # raise click.BadParameter
    if not output:
        output = click.get_binary_stream('stdout')

    # <file> input
    # TODO ValueError (when errors is 'strict')
    # raise click.FileError
    if file:
        text = file.read()

    # TTS
    try:
        tts = gTTS(text=text, lang=lang, slow=slow, lang_check=check, debug=debug)
        tts.write_to_fp(output)
    except ValueError as e:
        raise click.BadOptionUsage(str(e)) 
    except gTTSError as e:
        raise click.UsageError(str(e))
    except Exception as e:
        raise click.ClickException(str(e))
