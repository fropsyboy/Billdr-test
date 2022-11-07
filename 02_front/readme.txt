Goal: Create a simple web app that list users information from an API with ReactJs (~2h)

1) Create 2 simple html pages: "List page" + "Description page"
2) Fetch users on this endpoint -> "https://jsonplaceholder.typicode.com/users" and list the result on the "List page"
3) When clicking on a user on the list, it goes to the "description page" of the user fetched. Ex for user with ID 1 you need to fetch "https://jsonplaceholder.typicode.com/users/1"
4) You are totally free on the UI, don't spend time making it super fancy, but make it good enough.
Feel free (and recommended) to use a css frameworks (bulma, tailwind, bootstrap,...)

##Docmentation

Installation details - `./bulldr-test/README.md`

Screenshots for quick view - .`/bulldr-test/screenshots`

Assignment files - `./bulldr-test/src/screens/userList` - Question 02_front -> 1(a)
                 - `./bulldr-test/src/screens/userDescription` - Question 02_front -> 1(b)
                 - `./bulldr-test/src/screens/userList` - Question 02_front -> 2
                 - `./bulldr-test/src/screens/userDescription` - Question 02_front -> 3
                 -    Question 4 - I used pure `bootstrap` as the css framework

Test file - - `./bulldr-test/src/setupTest.js` : didn't set it up but just added the structure needed to set it up.
                tool - `jest` for test.

Env examples: file name - .env.development, .env : either is fine depending on your setup

REACT_APP_ENVIRONMENT=development
REACT_APP_BASE_URL=https://jsonplaceholder.typicode.com
REACT_APP_BASE_URL_AVATAR=https://ui-avatars.com/api
REACT_APP_BASE_GOOGLE_KEY=xxxxxxxxxxxx-FMPLxxxxCeyxxxxq-xxxxxxx

Assets: - ./bulldr-test/src/assets

### Added feature - Added the search feature: Onclick on the search button the app searching through the whole record.