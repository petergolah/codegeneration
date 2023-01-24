# CodeGeneration
## AI tools for coding


### Setup
prerequisites: git, [poetry](https://pypi.org/project/poetry/){target="_blank"}
```sh
git clone https://github.com/petergolah/codegeneration.git
cd codegeneration
poetry install
./codegeneration.sh
# or
ln -s codegeneration.sh ~/bin/cg
# then
cg
# once it asks for an API key it's fine
```

### OpanAI - Set up API access
- go to [openai.com](https://beta.openai.com/){target="_blank"} and create an account
- go to: Profile menu > View API keys > create an API key  
- paste it in the prompt when asked  
- it'll be stored in `api.key` (gitignored)

### Profiles
- open `config.yml` to see and edit
- enter `./codegeneration.sh profiles` to see profiles in the terminal as a numbered list (1-based)

### Usage
```sh
# transformation using defaults - it uses the first profile
$ ./codegeneration.sh give me a function that generates fibonacci numbers
```
```sh
# see all profiles - a 1-based list
$ ./codegeneration.sh profiles`
$ ./codegeneration.sh p`
```
```sh
# transformation with profile #2 - 1-based list, see above
$ ./codegeneration.sh --profile 2 give me a function that generates fibonacci numbers
$ ./codegeneration.sh -p2 give me a function that generates fibonacci numbers
```
