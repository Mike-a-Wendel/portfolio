---
title: Content Development Tools
publishDate: 2020-03-08 00:00:00
img: /portfolio/assets/python-samp.jpg
img_alt: Sample Python script in VSCode window
description: |
  Design, build, and deploy processes and tools to simplify day-to-day writing tasks and improve team efficiency so writers can focus of more critical work.
tags:
  - Automation
  - Developer docs
  - Strategy
---

| Writing Sample Type        | Read online                                                                                       | Download or Print                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| sortFiles.py Python script | [GitHub](https://github.com/Mike-a-Wendel/portfolio/blob/main/public/assets/scripts/sortFiles.py) | [Download](../../portfolio/assets/scripts/sortFiles.py) |
| Using sortFiles.py         | [Sample documentation](#using-sortfilespy)                                                        | [PDF](../../portfolio/assets/pdf/Using-sortFiles.pdf)   |

**Notes on the writing sample:** Please consider the following description, the included python sample, and the [Sample documentation](#using-sortfilespy) as the writing sample.

#### Background

Large sets of information (let’s call them libraries), written by multiple people, present unique challenges to ensure data integrity, consistency, and library-wide updates. Data integrity and consistency can often be handled through the appropriate use of source control, like implementation and enforcement of a branch model, branch protection rules, and code reviews in GitHub.

Processes and tools to manage library-wide updates independently of the work of individual writers can be critical to the effectiveness of a documentation team.

For example, say you need to run accessibility checks and fixes as part of a bid requirement for a contract. Involving the entire documentation team in this important work takes them away from other critical work. You could hire a contractor just to handle this task, but you’ll likely have to hire her again when yet another unexpected, urgent task comes up that your team doesn’t have the bandwidth to handle. Or you could rely on documentation tools and processes that are developed specifically for your library to help your writers do what they do best, provide real value to the product by delighting customers while addressing their needs. Not by doing mindless, repetitive tasks to scrub already written documentation.

#### Process

Developing processes and tools to simplify the work of documentation teams requires strategic thought as well as the ability to translate process logic into tools.

As a sample, consider this Python script, which sorts DITA XML files into separate folders based on the topicrefs in a DITA map. This is a simplistic example, and might be used as the first step in a process to test or make changes to one set of topics when all documentation source is stored in a monorepo.

---

### Using sortFiles.py

This script sorts files into folders based on topicrefs in a DITA map. It uses the BeautifulSoup library to parse the DITA map and extract the topicref elements. All topicrefs with the same map id will be copied into a specified target folder. When you run the script, you’ll be prompted to enter the path to the DITA map file, the content source folder, and the target folder.

#### Requirements

To run this script, you will need:

- [Python 3](https://www.python.org/downloads/) installed on your computer
- The [BeautifulSoup library installed](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) with the lxml library since the script parses DITA. You can install the lxml library and BeautifulSoup by running the following command in your terminal or command prompt:

  ```shell
  pip install lxml
  pip install beautifulsoup4
  ```

#### Usage

To use this script, you will need to provide the following information when prompted:

- The path to the DITA map file
- The path to the source folder containing the files to be sorted
- The path to the target folder where the sorted files will be stored

Here's an example of how you can run this program:

```shell
python sortFiles.py
```

The script will prompt you to enter the path to the DITA map file, the source folder, and the target folder.

#### Notes

- The script assumes that the file names in the source folder match the href attributes in the DITA map.
- The script will create the target folder if it doesn't exist.
- If a folder with the same name as a map id already exists in the target folder, that folder will be used instead of a new folder, which might overwrite existing files in the target folder.
- The program will copy the files from the source folder to the target folder, so the original files will still be available in the source folder.

---
