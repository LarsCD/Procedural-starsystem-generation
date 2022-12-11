"""
/////////////////////////////////////////////////////////////////////////////
DOCUMENTATION -- GUT v0.2.1

-----------------------------------------------------------------------------
Made by:            Lars C. Dijkgraaf
Version:            v0.2.1  (2-12-2022)
Destrubuted by:     LCDCode
-----------------------------------------------------------------------------
GUT (Graphical User-interface Tool) is a tool for quickly making a GUI for
terminal/console like output.
-----------------------------------------------------------------------------
COLOR [class]

    Use COLOR to return a specific ANSI color code:

    COLOR.{Fore, Back}.{color name}

    Examples:
        COLOR.Fore.red()
        COLOR.Back.blue()

    Use {Fore} or {Back} to specify foreground or background color change.
    The sellection of colors for foreground and background colors are as
    follows:

    {color name}    Description
    - BLACK:        Black
    - RED:          Red
    - GREEN:        Green
    - YELLOW:       Yellow
    - BLUE:         Blue
    - MAGENTA:      Magenta
    - CYAN:         Cyan
    - GRAY:         Gray (if used for backround, will be white and Fore text
                          will keep same color)

    - B_RED:        Bright red
    - B_GREEN:      Bright green
    - B_YELLOW:     Bright yellow
    - B_BLUE:       Bright blue
    - B_MAGENTA:    Bright magenta
    - B_CYAN:       Bright cyan
    - WHITE:        (Normal white color for Fore and Back)
-----------------------------------------------------------------------------
    GUT [class]

    Use GUT for GUI functionality.

    GUT.
        WINDOW_CLEAR():
            Use to clear the screen (windows only function).

        WINDOW_LINE(width, char):
            Use for a line of a specific width, {char} is the character you
            want to fill the line with.

        WINDOW_LINE_CUSTOM(width, text):
            Similar to GUT.WINDOW_LINE(), specify text to be displayed.

        WINDOW_TITLETAG(title, char):
            Use for printing a title. {char} is begin character (comes before
            the title).

        PRINT_SELECTION(selection, char):
            Use to present an input selection to the user, {selection} is a
            dict with dict = {'user_input_character', 'selection_text'}. Specifies an
            action to the player with selection from a menu or something
            simmilar.


        MENU_SELECT(title, selection, settings, text=False):
            Creates a graphical menu for user to easily see selection
            choices. Setting {text} as a string will result in text showing
            above the actual selection.

        DISPLAY_TEXT(title, text, settings, selection=False):
            Displays a text, {text} can be a string or a list of strings.
            A list of strings will grant the abillity to display paragraphs
            of text.


-----------------------------------------------------------------------------
    LCDCode
/////////////////////////////////////////////////////////////////////////////
"""

from os import system


class COLOR:
    class Fore:
        def BLACK():
            return '\033[0;90m'
        def RED():
            return '\033[31m'
        def GREEN():
            return '\033[32m'
        def YELLOW():
            return '\033[33m'
        def BLUE():
            return '\033[34m'
        def MAGENTA():
            return '\033[35m'
        def CYAN():
            return '\033[36m'
        def GRAY():
            return '\033[37m'
        def B_BLACK():
            return '\033[30m'
        def B_RED():
            return '\033[91m'
        def B_GREEN():
            return '\033[92m'
        def B_YELLOW():
            return '\033[93m'
        def B_BLUE():
            return '\033[94m'
        def B_MAGENTA():
            return '\033[95m'
        def B_CYAN():
            return '\033[96m'
        def WHITE():
            return '\033[97m'
        def RESET():
            return '\033[0m'

    class Back:
        def BLACK():
            return '\u001b[40m'
        def RED():
            return '\u001b[41m'
        def GREEN():
            return '\u001b[42m'
        def YELLOW():
            return '\u001b[43m'
        def MAGENTA():
            return '\u001b[44m'
        def CYAN():
            return '\u001b[45m'
        def BLUE():
            return '\u001b[46m'
        def GRAY():
            return '\u001b[47m'
        def B_BLACK():
            return '\u001b[40;1m'
        def B_RED():
            return '\u001b[41;1m'
        def B_GREEN():
            return '\u001b[42;1m'
        def B_YELLOW():
            return '\u001b[43;1m'
        def B_BLUE():
            return '\u001b[44;1m'
        def B_MAGENTA():
            return '\u001b[45;1m'
        def B_CYAN():
            return '\u001b[46;1m'
        def WHITE():
            return '\u001b[47;1m'
        def RESET():
            return '\u001b[0m'


class GUT:
    def __init__(self, settings):
        self.settings = settings

        # tool setup
        self.package_name = 'Graphical User-interface Tool (GUT)'
        self.package_version = 'v1.0'
        self.package_distributor = 'lcd'
        self.package_title = (f'[{self.package_name} | {self.package_version} | {self.package_distributor}]')
        print(self.package_title)

        # terminal dimensions
        self.window_width = settings['window']['window_width']
        self.window_height = settings['window']['window_height']



    def WINDOW_CLEAR():
        system('CLS')


    def WINDOW_LINE(width, char):
        print(char * (width))


    def WINDOW_LINE_CUSTOM(width, text):
        background = COLOR.Back.GRAY()
        color = COLOR.Fore.B_BLACK()
        reset = f'{COLOR.Fore.RESET()}{COLOR.Back.RESET()}'
        print(f'{background}{(color + text): <{width + 5}}{reset}')


    def WINDOW_TITLETAG(title, char):
        print(f'{char} [{title}]')


    def PRINT_SELECTION(selection, char):
        if type(selection) is list:
            multi = True
        else:
            multi = False
        if multi:
            for sub_select in selection:
                for s in sub_select:
                    if s == '/':
                        print(char)
                    else:
                        print(f'{char} [{COLOR.Fore.B_GREEN()}{s.capitalize()}{COLOR.Fore.RESET()}]: {sub_select[s]}')
                print(char)
        else:
            for s in selection:
                if s == '/':
                    print(char)
                else:
                    print(f'{char} [{COLOR.Fore.B_GREEN()}{s.capitalize()}{COLOR.Fore.RESET()}]: {selection[s]}')
            print(char)



    def MENU_SELECT(title, selection, settings, text=False):
        # settings dimensions
        window_width = settings['window']['window_width']
        window_height = settings['window']['window_height']
        char = settings['char']

        GUT.WINDOW_CLEAR()
        # GUT.WINDOW_LINE(window_width, char)
        GUT.WINDOW_LINE_CUSTOM(window_width, '')
        GUT.WINDOW_TITLETAG(title, char)
        print(char)
        if text != False:
            print(f'{char} {text}')
            print(char)
        GUT.PRINT_SELECTION(selection, char)
        GUT.WINDOW_LINE_CUSTOM(window_width, ' [Type \'/\' for commands, type \'/h\' or \'/help\' for list of commands]')



    def DISPLAY_TEXT(title, text, settings, selection=False):
        # settings dimensions
        window_width = settings['window']['window_width']
        window_height = settings['window']['window_height']
        char = settings['char']

        def get_chunks(text, maxlength):
            # takes one long string and cuts it into smaller size parts
            start = 0
            end = 0
            while start + maxlength < len(text) and end != -1:
                end = text.rfind(" ", start, start + maxlength + 1)

                yield text[start:end]
                start = end + 1
            yield text[start:]

        GUT.WINDOW_CLEAR()
        # GUT.WINDOW_LINE(window_width, char)
        GUT.WINDOW_LINE_CUSTOM(window_width, '')
        title = f'{COLOR.Fore.B_BLUE()}{title}{COLOR.Fore.RESET()}'
        GUT.WINDOW_TITLETAG(title, char)
        print(char)

        if type(text) is list:
            paragraph_list = []
            for part in text:
                chunks = get_chunks(part, (window_width - 4))
                text_list = [(n, len(n)) for n in chunks]
                paragraph_list.append(text_list)
            for part in paragraph_list:
                for line in part:
                    print(f'{char} {line[0]}')
        else:
            chunks = get_chunks(text, (window_width - 4))
            text_list = [(n, len(n)) for n in chunks]

            for line in text_list:
                print(f'{char} {line[0]}')
        print(char)
        if selection == False:
            print(f'{char} [{COLOR.Fore.B_GREEN()}ENTER{COLOR.Fore.RESET()}]: Close')
            print(char)
        else:
            GUT.PRINT_SELECTION(selection, char)
        GUT.WINDOW_LINE_CUSTOM(window_width, ' [Type \'/\' for commands, type \'/h\' or \'/help\' for list of commands]')

