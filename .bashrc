# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba init' !!
export MAMBA_EXE="/tmp/bin/micromamba";
export MAMBA_ROOT_PREFIX="/srv/conda";
__mamba_setup="$('/tmp/bin/micromamba' shell hook --shell bash --prefix '/srv/conda' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    if [ -f "/srv/conda/etc/profile.d/mamba.sh" ]; then
        . "/srv/conda/etc/profile.d/mamba.sh"
    else
        export PATH="/srv/conda/bin:$PATH"
    fi
fi
unset __mamba_setup
# <<< mamba initialize <<<
