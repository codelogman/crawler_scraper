# Generative AI Synaptic System. Crawler and Classifier Modules

This repository contains the implementation of an advanced generative artificial intelligence system that includes a web crawler and a dynamic classifier. The system is designed to efficiently and automatically collect and analyze web content.

## Description

The system consists of two main components:
1. **WebCrawler**: A web crawler that searches for and collects content from the Internet based on dynamically updated keywords. This component respects website policies and adjusts its searches in real time to focus on the most relevant areas.
2. **ContentClassifier**: A classifier that uses natural language processing (NLP) techniques to categorize the collected content and provide feedback to the crawler about which topics require more attention.

## Features

- **Automated Content Search**: Uses dynamically updated keywords to locate and collect relevant information.
- **Adaptability**: Capable of modifying its search parameters in real time based on feedback from the classifier.
- **Efficiency and Respect for Websites**: Implements courtesy policies to avoid overloading web servers and respects `robots.txt` files.
- **Dynamic Feedback and Classifier Integration**: Receives instructions from the classifier on what topics to search for and adjusts its activities based on processed and categorized information.

## Repository Structure

- `WebCrawler.py` - Contains the implementation of the web crawler.
- `ContentClassifier.py` - Contains the implementation of the dynamic classifier.
- `README.md` - This file.

## Requirements

To run the scripts, you will need Python 3.8 or higher, along with the following libraries:
- `pymongo`
- `requests`
- `beautifulsoup4`
- `scikit-learn`

## Installation

Clone this repository to your local machine using:
```bash
git clone <repository-url>
