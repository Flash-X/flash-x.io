# Install developer enviornment

### Ubuntu
```
sudo apt install ruby ruby-dev
sudo apt install gem
sudo gem install jekyll bundler
sudo bundle install
./server
```

### Mac 
```
brew install ruby
-----Depending on whether you are running zsh or bash 
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.0.0/bin:$PATH"' >> ~/.zshrc
-----or
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.0.0/bin:$PATH"' >> ~/.bash_profile
------ this is an important step because OSX comes with its own ruby"
gem install jekyll bundler
bundle add webrick --- this is needed because ruby3.0 does not have webrick
bundle install
./server
```
