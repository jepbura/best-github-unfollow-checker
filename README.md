<br>

<h1 align="center">
  🥇 Best Github Unfollow Checker 🥇
</h1>

<p align="center"><img src="https://raw.githubusercontent.com/jepbura/best-github-unfollow-checker/main/assets/images/unfollow.png" alt="E2F" /></p>

<h3 align="center">
  This project is used to find all those who unfollowed you
</h3>

## Why is this project the best unfollow checker on GitHub?

This is because it 🤖 automatically checks the status of your followers every day at a certain time and automatically unfollows the people who unfollowed you.

## Usage

Specify the environmental variable to set up project configurations.(**settings => secrets => actions**)

| Variable            | Description                                      | example                           |
| ------------------- | ------------------------------------------------ | --------------------------------- |
| **USERNAME**        | Your username to check followers                 | jepbura                           |
| **IGNORE_LIST**     | List of people who are exceptions to unfollowing | jepbura,flutter,kubernetes,docker |
| **GH_ACCESS_TOKEN** | Your github access token                         | **\*\*\***                        |

## Note

1- **IGNORE_LIST** contains an exception list that you don't want these people to unfollow.
**Be sure to use the symbol {,} to separate the names**

2- Visit [ACCESS_TOKEN](https://github.com/settings/tokens?type=beta), generate a new token, specify a name and expiration, choose your repositories (only select repositories), and ensure to set **Read and write** for **Followers** in the Permissions section.

## Contact Us

<hr>

<p align="center">
  <a href="https://www.bura.dev">
    <img alt="GitHub Profile Readme Generator" src="/assets/images/logo.png" width="60" />
  </a>
</p>

<p align="center">
Developed with <a href='https://www.bura.dev' target='_blank'>BURA</a> ❤️
</p>

## License

This project is licensed under the [MIT License](LICENSE).
