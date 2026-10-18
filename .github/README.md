# dotfiles

macOS dotfiles, managed as a bare git repo in `~/.dotfiles` with `$HOME` as the work tree.

| File | What |
|---|---|
| `.zshrc`, `.zprofile`, `.zshenv` | zsh + oh-my-zsh + powerlevel10k |
| `.p10k.zsh` | prompt config |
| `.tmux.conf` | tmux (prefix `C-a`, plugins via tpm) |
| `.gitconfig`, `.config/git/ignore` | git |
| `.config/nvim` | neovim (submodule → [julio-nvim](https://github.com/JulioPeixoto/julio-nvim)) |
| `.config/fastfetch` | fastfetch |
| `.config/dotfiles/cursor-extensions.txt` | Cursor/VS Code extensions |

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/JulioPeixoto/dotfiles/main/.config/dotfiles/install.sh | bash
```

## Usage

```sh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
dotfiles status
dotfiles add ~/.tmux.conf && dotfiles commit -m "..." && dotfiles push
```
