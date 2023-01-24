from rich import print as richprint
import util


def on_no_command(quickparse):
    if quickparse.args:
        profile_index = None
        if '--profile' in quickparse.options:
            try:
                profile_index = int(quickparse.options['--profile'])
            except:
                raise AssertionError(f"Invalid profile index: {quickparse.options['--profile']}")
        util.make_openai_api_request(' '.join(map(str, quickparse.parameters)), profile_index)
    else:
        show_help()

def show_help():
    richprint(util.help_text)

def show_profiles(quickparse):
    assert len(quickparse.parameters) <= 1, "Too many parameters, 'profiles' goes without any"
    if len(quickparse.parameters) == 1:
        try:
            profile_index = int(quickparse.parameters[0])
        except:
            raise AssertionError(f"Invalid profile index: {quickparse.parameters[0]}")
        util.update_profile_index(profile_index)
    util.print_profiles()
