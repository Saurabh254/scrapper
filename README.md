<p align="center">
  <a href="" rel="noopener">
  <pre>
 ____
/ ___|  ___ _ __ __ _ _ __  _ __   ___ _ __
\___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
 ___) | (__| | | (_| | |_) | |_) |  __/ |
|____/ \___|_|  \__,_| .__/| .__/ \___|_|
                     |_|   |_|
</pre>
 </a>
</p>

<h3 align="center">Scapper</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Saurabh254/scrapper)](https://github.com/Saurabh254/scrapper/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Saurabh254/scrapper)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">
    Scrapper is the backend for our Real time notifier project. Scrapper uses bs4 module to parse the data and shipped it through the network in json format using fastapi.
    <br>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🎈 Usage ](#-usage-)
- [🚀 Deployment ](#-deployment-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

The Purpose of the Scrapper is to scrap the real time data from the internet and parse it for further uses.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Clone the repository by the running the command in the terminal.

```py
git clone https://www.github.com/Saurabh254/Scrapper
```

### Installing

A step by step series of examples that tell you how to get a development env running.

creating a virtual environment

```
python -m venv virt
```
activating virtual environment

```
source virt/bin/activate
```
Installing the packages
```
pip install -r requirements.txt
```
start the api

```
python -m src
```

you'll see like this

```log
(virt) [saurabh254@Saurabh-PC scrapper]$ python -m src
INFO:     Started server process [22930]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
now open this url on your browser

Url : [http://127.0.0.1:8000/pocox4](http://127.0.0.1:8000/poco%20x4)

<!-- ## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Postgres](https://www.mongodb.com/) - Database
- [Fastapi](https://expressjs.com/) - Server Framework
- [BeautifulSoup](https://vuejs.org/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@Saurabh254](https://github.com/Saurabh254) - Idea & Initial work

See also the list of [contributors](https://github.com/Saurabh254/Scrapper/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
