# coding-profile-server

A modular, extensible server for fetching coding profile data from various platforms. Built with Python and FastAPI, it currently supports LeetCode and is designed to be easily extended to other coding platforms.

## Features

- **Modular architecture:** Add support for new coding platforms easily.
- **FastAPI powered:** Asynchronous, high-performance REST API.
- **LeetCode integration:** Fetch detailed stats for any LeetCode user.
- **GraphQL support:** (Planned/Partial, see roadmap)
- **Extensible:** Platform logic is separated for future integrations.

## Supported Endpoints

All endpoints are grouped under `/leetcode` for the LeetCode platform.

| Route                                 | Description                              |
|----------------------------------------|------------------------------------------|
| `/leetcode/{username}/info`           | Get general info about the user          |
| `/leetcode/{username}/stats`          | Get language stats for the user          |
| `/leetcode/{username}/tags`           | Get problem counts by tag                |
| `/leetcode/{username}/rating`         | Get contest rating info                  |
| `/leetcode/{username}/histogram`      | Get contest rating histogram             |
| `/leetcode/{username}/solved`         | Get information about solved problems    |
| `/leetcode/{username}/badges`         | Get badge information                    |
| `/leetcode/{username}/submissions`    | Get recent accepted submissions          |
| `/leetcode/{username}/discussions`    | Get user discussion solutions            |

> More routes and platform support can be added by plugging in new routers and controllers.

## Structure

- `app/routers/leetcode_router.py`: Defines all LeetCode-specific routes.
- `app/controllers/LeetCodeController.py`: Implements the business logic for LeetCode data fetching.
- `app/`: Designed for modularity—new platforms can be added under `routers/` and `controllers/`.

## How to Run

1. Clone the repository
    ```bash
    git clone https://github.com/abhinandanmishra1/coding-profile-server.git
    cd coding-profile-server
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server
    ```bash
    uvicorn app.main:app --reload
    ```

## Roadmap

- [x] Support for LeetCode
- [ ] Add support for other platforms (e.g., Codeforces, HackerRank)
- [ ] Full GraphQL API
- [ ] Authentication and user management

## Extending to Other Platforms

To add a new platform:
1. Create a new router in `app/routers/`.
2. Implement the controller logic in `app/controllers/`.
3. Register the router with the server in `app/main.py`.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is currently unlicensed. Please contact the repository owner for license inquiries.

---

> **Note:** The above endpoints and structure are based on the current state of the repository. [View more code details here.](https://github.com/abhinandanmishra1/coding-profile-server/search?q=router)
