# Local Development Setup

This project uses the [`github-pages`](https://rubygems.org/gems/github-pages) gem to pin the same Ruby toolchain that powers GitHub Pages. Follow the steps below to prepare a working environment on Linux and macOS 15.6.

## 1. Prerequisites

| Requirement | Recommended version |
|-------------|---------------------|
| Ruby        | 3.1.x or 3.2.x (>= 2.7 required by GitHub Pages dependencies) |
| Bundler     | 2.4.19 |
| Node.js     | Optional, only needed if you want to manage front-end assets |

> **Why Ruby ≥ 2.7?** Recent versions of Nokogiri bundled with `github-pages` need Ruby 2.7 or newer. Ruby 2.6 will fail with the error shown in the issue description.

Choose one Ruby version manager (rbenv, asdf, ruby-install/chruby, or mise) and ensure it is active in your shell before continuing.

## 2. Linux setup (Ubuntu/Debian example)

1. Install system dependencies:
   ```bash
   sudo apt update
   sudo apt install -y build-essential curl git libssl-dev libreadline-dev zlib1g-dev
   ```
2. Install Ruby (pick one option):
   * **mise** (recommended in this repo):
     ```bash
     curl https://mise.jdx.dev/install.sh | sh
     echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
     ~/.local/bin/mise use --global ruby@3.2.3
     ```
   * **rbenv**:
     ```bash
     curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash
     echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
     echo 'eval "$(rbenv init - bash)"' >> ~/.bashrc
     exec $SHELL
     rbenv install 3.2.3
     rbenv global 3.2.3
     ```
3. Update RubyGems and install Bundler 2.4.19:
   ```bash
   gem update --system
   gem install bundler -v 2.4.19
   ```
4. Install project dependencies and start the development server:
   ```bash
   bundle install
   bundle exec jekyll serve
   ```
   The site will be available at <http://127.0.0.1:4000>.

## 3. macOS setup (15.6 Sonoma)

1. Install Xcode command line tools:
   ```bash
   xcode-select --install
   ```
2. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Ruby and dependencies. Pick one of the following approaches:
   * **mise**:
     ```bash
     brew install mise
     echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
     mise use --global ruby@3.2.3
     ```
   * **rbenv**:
     ```bash
     brew install rbenv ruby-build
     echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
     rbenv install 3.2.3
     rbenv global 3.2.3
     ```
4. Update RubyGems and install Bundler 2.4.19:
   ```bash
   gem update --system
   gem install bundler -v 2.4.19
   ```
5. Install dependencies and run the site:
   ```bash
   bundle install
   bundle exec jekyll serve --livereload
   ```
   The server will run at <http://127.0.0.1:4000>. The `--livereload` flag automatically refreshes the browser when files change.

## 4. Useful commands

| Command | Description |
|---------|-------------|
| `bundle exec jekyll serve` | Start a local preview server |
| `bundle exec jekyll build` | Generate the static site into `_site/` |
| `bundle update` | Refresh locked dependencies (only when intentionally updating the stack) |
| `bundle exec jekyll doctor` | Run health checks on the site configuration |

## 5. Troubleshooting

* **Bundler version mismatch** – Run `gem install bundler -v 2.4.19` and rerun `bundle install`.
* **Native extension build failures** – Ensure build tools are installed (see step 2 on Linux, Xcode CLT on macOS).
* **Port already in use** – Start the server on another port: `bundle exec jekyll serve --port 4001`.

With this setup, your local environment matches the latest tool versions supported by GitHub Pages (`github-pages` 228 with Jekyll 3.9.3).
