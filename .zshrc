# Theme configuration
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel9k/powerlevel9k"

plugins=(git)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status)

source $ZSH/oh-my-zsh.sh

# History configuration
HISTSIZE=1000000000
SAVEHIST=1000000000
HIST_STAMPS="yyyy-mm-dd"

# SSH agent configuration
if [ -z "$SSH_AUTH_SOCK" ] ; then
    eval `ssh-agent -s`
    ssh-add
fi

# Nvm configuration
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Custom aliases
alias vim="vim -p"
alias code="code ."
