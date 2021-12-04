/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install pyenv
pyenv install 3.9.8
pyenv global 3.9.8
pip3 install pyinstaller