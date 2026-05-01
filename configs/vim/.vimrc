" Vim: ~/.vimrc: startup settings for vim
" Nvim: ~/.config/nvim/init.vim 

" Use Vim features: do not restrict ourselves to pure vi.
set nocompatible

" No annoying beeps.
set noerrorbells
set visualbell

" We want to always show the status line at the bottom of the pane.
" It should show (upto 50 chars of) the filename, modified (or, read-only) status.
" In the right corner, show the file type, row, col number and percent thru the file.
set laststatus=2
set statusline=%.50F\ %m\ %R
set statusline+=%=%Y\ [%l:%c]\ [%p%%]

" Syntax highlighting, file type recognition, UTF-8 format (for display).
syntax on
filetype on
filetype indent on
set encoding=utf-8

" I like spaces not tabs, so expand tabs to (2) spaces. 
" Indent by the same when formatting code.
set tabstop=2
set shiftwidth=2
set expandtab

" Show commands as they are entered on the command line,
" and show the mode in the status area (e.g., 'INSERT').
set showcmd
set showmode

" Highlight matching closures, e.g., parentheses or comment markers.
" We use the matchit package (included with recent Vim) so that
" we get %-matching on things like XML, shell, and LaTeX.
packadd! matchit

" When searching, highlight all the matches, and highlight the matches as the
" pattern is searched. Ignore case unless an uppercase search pattern is used.
set incsearch
set hlsearch
set ignorecase
set smartcase

" Show the current cursor position with a highlighted row/column.
set cursorline
set cursorcolumn

" Basic color scheme.
" colorscheme morning
colorscheme evening

" Display dark gray column rulers at 80, 100, and 120 chars.
" 80 chars is old-school, 100 is comfortable on modern displays.
" That said, if you are still typing at 120 chars, you're doing it wrong!
" To enforce better practice, insert a break (newline) if I attempt 
" to type such long lines.
set colorcolumn=80,100,120
highlight colorcolumn guibg=darkgray
highlight colorcolumn ctermbg=7

set textwidth=120
set formatoptions+=t

" The end.
