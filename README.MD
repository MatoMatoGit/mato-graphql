# mato-graphql
## COMMANDS

### Install virtual environment
`$ pip install virtualenv`

### Alias virtual environment
`$ virtualenv venv`

### Enter virtual environment
`$ source venv/bin/activate`

### Install tools in virtual environment
`$ pip install -r requirements.txt`

### Run python server
`$ python app.py runserver`

# Queries
`{
  createPost(username:"johndoe", title:"Hello 2", body:"Hello body 2"){
    post{
      title
      body
      author{
        username
      }
    }
  }
}`