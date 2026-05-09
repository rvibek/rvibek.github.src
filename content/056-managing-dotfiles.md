Title: Managing dotfiles with GNU Stow
Slug: manage-dotfiles-with-gnu-stow
Date: 2026-05-09 20:20
Modified: 2026-05-09 20:20
Category: Blog
Tags:  dotfiles, GNU Stow, config management, productivity, ai
Author: Vibek Raj Maurya
Summary: This post covers how GNU Stow turned a scattered mess of dotfiles into a clean, Git-tracked system. Stow creates symlinks from your home directory to a single ~/dotfiles folder, letting you enable or disable configs for any app with one command.


I used to have config files scattered all over my home directory — .zshrc here, .gitconfig there, random stuff in .config/. No version control, no single source of truth. The real pain hit when I'd tweak something on my MacBook Pro, then have to remember to do the same dance on the Mac Mini and my WSL workstation. Three machines, three copies of the same mess, zero sync. It was a nightmare.
Then I found [GNU Stow](https://www.gnu.org/software/stow/), and it changed everything.

Stow is a symlink farm manager. Fancy name, simple idea: you keep all your dotfiles in one tidy folder (`~/dotfiles`), and Stow creates symlinks from your home directory pointing back to it. Your configs stay organized, Git-trackable, and portable across machines.

The best part? You can enable or disable entire app configs with a single command.

Install it quick:

```bash
# Debian/Ubuntu
sudo apt install stow

# macOS
brew install stow

```

## The workflow in 30 seconds

1. Create `~/dotfiles`
2. Make a subdirectory (a "package") for each app
3. Move your config files into the matching directory structure
4. Run `stow <package>` from inside `~/dotfiles`

That's it. Let me show you what this looks like in practice.

## Stowing `.zshrc`

ZSH config lives at `~/.zshrc`. Here's the move:

```bash
cd ~/dotfiles

# Move your existing config in
mv ~/.zshrc .

# Stow it
stow zsh
```

Stow creates a symlink: `~/.zshrc → ~/dotfiles/.zshrc`. You edit the file in either location — it's the same file.

Got more ZSH files? Throw them in:

```bash
mv ~/.zsh_aliases .
mv ~/.zsh_functions .
stow -R    # Restow to pick up new files
```

Your package now looks like:

```
~/dotfiles/
├── .zshrc
├── .zsh_aliases
└── .zsh_functions
```

## Stowing OpenCode 

Editors like OpenCode keep config under `~/.config/opencode/`. The key here is mirroring the directory structure inside your package:

```bash
cd ~/dotfiles
mkdir -p opencode/.config/opencode

mv ~/.config/opencode/* opencode/.config/opencode/

stow opencode
```

Now `~/.config/opencode` is a symlink pointing into your dotfiles. Your settings, keybindings — all tracked:

```
~/dotfiles/
└── .config/
  └── opencode/
    ├── opencode.jsonc
    ├── package.json
    └── skills
```

Same pattern works for any app that stores config under `~/.config/` — Yazi, Newsboat, whatever you use. Create the package, mirror the path, stow it.

## Version control with Git

This is where Stow really earns its keep. Your entire `~/dotfiles` folder is just a regular directory — perfect for Git.

```bash
cd ~/dotfiles
git init
git add .
git commit -m "init"

git remote add origin git@github.com:rvibek/dotfiles.git
git push -u origin main
```

Add a `.gitignore` to keep things clean:

```gitignore

.DS_Store
*.swp
*~
*.db
*.lock

```

Day-to-day, the flow is dead simple — edit a config, commit, push:

```bash
git add zsh/.zshrc
git commit -m "Update zsh aliases"
git push
```

## Setting up a new machine

This is the killer feature. Fresh system? Five commands:

```bash
brew install stow
git clone git@github.com:rvibek/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow zsh opencode
```

Done. Your entire environment is back. And you can be selective — only stow what you need on that particular machine.


## Commands worth remembering

- `stow <pkg>` — create symlinks
- `stow -D <pkg>` — remove symlinks
- `stow -R <pkg>` — restow (useful after adding files)
- `stow -n -v <pkg>` — dry run, see what would happen
- `stow */` — stow every package at once

## Quick troubleshooting

**"Cannot stow over existing file"** — a real file is in the way. Move it into your package first, then restow:

```bash
mv ~/.zshrc ~/dotfiles/zsh/
stow -R zsh
```

Happy stowing. ✌️
