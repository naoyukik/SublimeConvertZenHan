import sublime_plugin
from .jaconv.jaconv import h2z, z2h


class ConvertZenHanCommand(sublime_plugin.TextCommand):
    def run(self, edit, to, kana=False, ascii=False, digit=False):
        sels = self.view.sel()
        for sel in sels:
            selection_word = self.view.substr(sel)
            if to == 'zen':
                result = h2z(selection_word, '', kana, ascii, digit)
            else:
                result = z2h(selection_word, '', kana, ascii, digit)

            self.view.replace(edit, sel, result)
