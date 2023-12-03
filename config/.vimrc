let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()
  Plug 'tpope/vim-sensible'
  Plug 'davidhalter/jedi-vim'
  Plug 'preservim/nerdtree'
call plug#end()

# Basic Vim conf
set number
syntax enable
filetype indent on
set tabstop=4
set softtabstop=4
set autoindent
set encoding=utf-8
colorscheme ron
nnoremap <C-t> :terminal<CR>

# Python specific config
nnoremap py :!python %

# NerdTree mapings
nnoremap w:<C-w><C-w>
