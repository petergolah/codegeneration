# CodeGeneration
## AI tools for coding


### Setup
prerequisites: git, poetry
```sh
git clone https://github.com/petergolah/codegeneration.git
cd codegeneration
poetry install
./codegeneration.sh
# or
ln -s codegeneration.sh ~/bin/cg
# then
cg
# first time it complains about missing API key, keep reading
```
### OpenAI

#### Set up API access
Generate API key at [openai.com](https://beta.openai.com/){target="_blank"}.  
Put it in `api.key`
