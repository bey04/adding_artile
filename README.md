# Blog Platform

A simple blog platform that allows users to add and view articles.

## Features
- Add new articles.
- View a list of articles.
- Store articles in a MySQL database.

## Getting Started

### Prerequisites
- Python 3.x
- MySQL server

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bey04/blog_platform.git
   cd blog_platform

### creation db
CREATE DATABASE blog_db;

USE blog_db;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
