# Emoji Keygen

Fullstack application that uses Flask/Postgresql on the backend and React on the frontend. It generates 64 character hex keys (mocking Ethereum private keys), converts them into emojis (specifically using a maximum of 29 to maintain base-29), and returns this result to the client. The client can submit the emoji sequence to reobtain the information that was provided upon generation.

### Running

The project is containerized and should be run with docker-compose. Once the client is running (after react-scripts is started), the interface can be found at http://localhost:3000/

```
docker-compose up --build
```

### Endpoints

Connected to http://localhost:5000/

```
POST /emoji
```

Provided a name, the endpoint will return an emoji sequence that is associated with a private key. The private key is stored in the database as the primary key to the name provided.

Arguments in body:

| Parameter | Type     | Description                                                          |
| --------- | -------- | -------------------------------------------------------------------- |
| `name`    | `string` | **Required**. Information you want associated with the generated key |

---

```
GET /info
```

Provided an emoji sequence, the endpoint will decode it and search for an existing key. If found, the related contents will be returned.

Query parameters:

| Parameter | Type             | Description                                                     |
| --------- | ---------------- | --------------------------------------------------------------- |
| `key`     | `emoji sequence` | **Required**. The sequence that will be decoded and queried for |

---

```
GET /all
```

FOR TESTING PURPOSES. This endpoint will return everything in the database to show how information is stored.

No params.

## Design Decisions

### Server

Server is built with flask because it's the simplest and most lightweight framework I'm somewhat familiar with in python. The backend generates a 64 character key using the built-in randbits function and converts this to a hex string. I didn't use an actual ethereum framework because conceptually it should be the same. The key undergoes a standard base conversion into base-29. The base-29 values are then mapped into a predefined emoji language (29 emojis). This Emoji sequence is returned in the api call. The key also is hashed using keccak hash from pycryptodome. This hash is stored in the database as the primary key. The remaining columns are the name and other info that would be provided.

\*\*Any one-way function would've worked. The idea here was to save an image of the private key without storing the actual key as that would make for a high security risk. Noted difficulties with this solution is that there's no surrounding account management (storing emails, phone numbers) therefore if this emoji sequence is lost, then the user will not be able to retrieve their information. Also the direct conversion from base 16 to base29 only reduces the length of the key ~11 characters.

I opted to start with the emoji challenge to setup the framework of the application. Next step is implementing the suggested markov chain for sentence keys (will follow up with clarifications about this.)

### Client

Connected to http://localhost:3000/

The client is built in react. There's nothing special going on here. I created a really basic interface for a user to input their name and call the emoji endpoint. The returned emoji sequence can be passed back into a different field where their name will be returned.
