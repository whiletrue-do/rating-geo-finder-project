# Rating Geo Finder Project

## Introduction

The Rating Geo Finder Project is a dynamic endeavor aimed at fulfilling a specific request: the ability to search for restaurants based on a particular rating using Google's services. This project will evolve over time as we conduct investigations and uncover the necessary functionality to meet the project's objectives.

## Guide to Enabling Google Places API (New)

Google Places API (New) allows you to access a wealth of location-based data for your applications. To begin using it, follow these steps to enable the API in your Google Cloud project:

### Prerequisites

Before you start, make sure you have the following:

1. A Google Cloud Platform (GCP) account: If you don't have one, you can create it at [Google Cloud Console](https://console.cloud.google.com/).

2. A project in Google Cloud Console: Create a new project or use an existing one.

### Enabling Google Places API (New)

1. Open the [Google Cloud Console](https://console.cloud.google.com/).

2. Select your project (or create a new one) using the project selector in the top bar.

3. In the left sidebar, click on "APIs & Services" and then "Dashboard."

4. Click the "+ ENABLE APIS AND SERVICES" button at the top of the page.

5. In the search bar, type "Places API (new)" and select it from the results.

6. Click the "Enable" button to enable the Google Places API (New) for your project.

7. Once the API is enabled, you can configure its settings and access its documentation by clicking on the "Manage" button.

### Creating Credentials

After enabling the API, you'll need to create credentials to access it securely:

1. In the Google Cloud Console, navigate to your project and select "APIs & Services" > "Credentials."

2. Click the "+ CREATE CREDENTIALS" button and select "API Key."

3. A new API key will be generated for you. You can customize its settings and restrictions if needed:

   - **Name**: Provide a name for your API key to identify its purpose.
   - **Restrictions**: Consider setting restrictions such as IP addresses or specifying which APIs it can access.

4. Click the "Create" button.

5. Your API key will be generated and displayed. Be sure to copy it and store it securely, as you won't be able to see it again.

### Restricting API Key Access (Optional)

For added security, you can restrict the usage of your API key.

As part of this project we will expand on this later in terms of best practices.

## Configuration

In this section, we will continuously update the required configuration setup to ensure the project's smooth operation.

### .env File

For managing various layers of configuration, we have chosen to employ Python's implementation of `dotenv`. This versatile package enables us to securely store key-value pairs in a file named `.env`. You can find more information about the `python-dotenv` package [here](https://pypi.org/project/python-dotenv/).

#### Why Environment Variables?

Environment variables are an essential aspect of modern software development for several reasons:

1. **Security**: By storing sensitive information such as API keys, database credentials, and other secrets in environment variables, we reduce the risk of exposing this information in code repositories or public spaces.

2. **Flexibility**: Environment variables allow us to change configuration parameters without modifying the source code. This flexibility is particularly useful when deploying the project to different environments (development, testing, production).

3. **Portability**: By abstracting configuration into environment variables, we make our code more portable. It can run on various systems and environments without modification i.e. linux, Windows, etc.

4. **Version Control**: Configuration files like `.env` are typically excluded from version control systems like Git, preventing accidental commits of sensitive data.

5. **Scalability**: As the project evolves and requires additional configuration settings, it's easy to update environment variables without changing the core codebase.

## creating your .env for this project

First of all at the root of this project create a file called `.env`.

```ini
# API Keys
google_maps_api_key={place api key here}

# Google Maps API Endpoints
places_text_new_search=https://places.googleapis.com/v1/places:searchText
```
