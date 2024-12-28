Shoppin Backend Reference Document
Objective
The purpose of this Assignment 6: Backend Engineer role, is to design and implement a web crawler tasked with discovering and listing all product URLs across multiple e-commerce websites. The main objectives and expected learning outcomes are:

Develop a scalable and efficient web crawler.
Handle diverse URL patterns and structures used by different e-commerce platforms.
Manage large sets of data and deep website hierarchies.
Implement parallel or asynchronous crawling to enhance performance.
Address specific edge cases like infinite scrolling and dynamically loaded content.
Produce a well-structured list of discovered product URLs mapped to their respective domains.
Step-by-Step Instructions
Project Setup and Initialization
Set Up the Project Directory:

Create a root directory for the project.
Initialize a Git repository within the root directory for version control.
Initialize the Project:

Create a virtual environment for the project to manage dependencies.
Initialize the project using relevant tools and frameworks (e.g., npm, pip, or others depending on the language used).
Install Dependencies:

List and install necessary dependencies such as libraries for web scraping (BeautifulSoup, Scrapy), HTTP requests (requests), and parallel processing (e.g., asyncio for Python).
Document all dependencies in a requirements file (requirements.txt) for Python or package.json for Node.js.
Development Process
Design the Crawler Architecture:

Plan the architecture of the web crawler, including modules for URL discovery, handling different URL patterns, and managing concurrency.
Implement URL Discovery:

Develop a function or module to identify and extract product URLs based on common patterns.
Ensure the function can adapt to different patterns (e.g., /product, /item, /p).
Handle Website Variations and Edge Cases:

Implement logic to manage infinite scrolling and dynamically loaded content using techniques like scrolling emulation or AJAX request simulation.
Design a solution to handle different URL structures and variations across e-commerce platforms.
Ensure Scalability and Performance:

Implement parallel or asynchronous processing to improve the crawler's efficiency.
Optimize the crawler to handle large domains with numerous products and deep hierarchies.
Output Formatting:

Develop a method to compile the discovered URLs into a structured format, mapping each domain to its respective list of product URLs.
Ensure that all URLs are unique and point directly to product pages.
Styling and Design
Documentation:

Create comprehensive documentation explaining the approach to finding product URLs.
Include descriptions of each module, function, and significant blocks of code.
Code Quality:

Ensure that the code is well-structured, readable, and adheres to best practices and coding standards.
Use descriptive variable names and include comments where necessary to enhance readability.
Deployment
Choose a Suitable Platform:

Select a platform for deploying the project, such as AWS, Heroku, or others depending on project needs and preferences.
Configure the Environment:

Set up the deployment environment, installing all necessary dependencies.
Ensure that environment configurations (e.g., API keys, database connections) are correctly set up and secured.
Deploy the Project:

Follow the platform-specific guidelines to deploy the project.
Test the deployment to ensure that the crawler runs correctly in the production environment.
Submission Guidelines
Github Repository:

Create a public or private repository on GitHub for the project.
Include all source code, along with the documentation of the approach for finding product URLs.
Ensure the repository is well-organized with a clear README file explaining the project setup and usage.
Structured List or File:

Generate a structured list or file containing all the discovered product URLs for each domain.
Format the output to map each domain to its corresponding list of product URLs, ensuring the URLs are unique and point directly to product pages.
Video Recording:

Record a video using a tool like loom.com, explaining the approach and providing a walkthrough of the code.
Ensure the video is clear, concise, and covers all significant aspects of the project.
Important Notes
Ensure that the submission does not include any unnecessary files or data.
Maintain a professional and clear structure in all documentation and outputs.
Follow the provided guidelines strictly to ensure a successful and efficient evaluation.
