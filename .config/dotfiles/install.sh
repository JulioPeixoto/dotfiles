#!/usr/bin/env bash
# Bootstrap dotfiles on a new macOS machine.
#   curl -fsSL https://raw.githubusercontent.com/JulioPeixoto/dotfiles/main/.config/dotfiles/install.sh | bash
set -euo pipefail

REPO="git@github.com:JulioPeixoto/dotfiles.git"
DOTDIR="$HOME/.dotfiles"
dot() { /usr/bin/git --git-dir="$DOTDIR" --work-tree="$HOME" "$@"; }

# homebrew
if ! command -v brew >/dev/null; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi
brew install git neovim tmux fastfetch

# dotfiles (bare repo)
if [ ! -d "$DOTDIR" ]; then
  git clone --bare "$REPO" "$DOTDIR"
  dot config status.showUntrackedFiles no
  if ! dot checkout 2>/dev/null; then
    backup="$HOME/.dotfiles-backup-$(date +%s)"
    echo "Backing up conflicting files to $backup"
    dot checkout 2>&1 | awk '/^\t/ {print $1}' | while read -r f; do
      mkdir -p "$backup/$(dirname "$f")" && mv "$HOME/$f" "$backup/$f"
    done
    dot checkout
  fi
  dot submodule update --init --recursive
fi

# oh-my-zsh + theme/plugins
[ -d "$HOME/.oh-my-zsh" ] || \
  RUNZSH=no KEEP_ZSHRC=yes sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
[ -d "$ZSH_CUSTOM/themes/powerlevel10k" ] || \
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "$ZSH_CUSTOM/themes/powerlevel10k"
[ -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ] || \
  git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"

# tmux plugin manager (then press prefix + I inside tmux)
[ -d "$HOME/.tmux/plugins/tpm" ] || \
  git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm"

# editor extensions (Cursor / VS Code)
if command -v code >/dev/null; then
  xargs -n1 code --install-extension < "$HOME/.config/dotfiles/cursor-extensions.txt"
fi

echo "Done. Open a new terminal."
