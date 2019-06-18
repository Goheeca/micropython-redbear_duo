from _utils import ansiEscaper, walk, print_file, fsstat
#ansiEscaper.enable(False)

ansiEscaper.set(ansiEscaper.Color.RED_BRIGHT)
print_file('/banner.txt')
ansiEscaper.reset()

print()
ansiEscaper.set(7)
print('FILESYSTEM', end='')
ansiEscaper.set(ansiEscaper.Color.BLACK_BRIGHT)
stat = fsstat()
print('{:6.02f}%'.format(100*(stat['blocks']-stat['free_blocks'])/stat['blocks']))
ansiEscaper.reset()

walk('/')

print()
ansiEscaper.set(7)
print('MODULES')
ansiEscaper.reset()
ansiEscaper.set(ansiEscaper.Color.CYAN_BRIGHT)
help('modules')
ansiEscaper.reset()

del ansiEscaper, walk, print_file, fsstat
