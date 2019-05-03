# YouTube

## Assignment Overview

This assignment will give you more experience on the use of:
1. classes
2. class methods

The goal of this project is to become more comfortable with creating and using various types of classes together. Knowing how to create and manage multiple instances of a class is important to leverage the power of object-oriented programming. This project will give you the opportunity to construct a series of classes that manage one another.

Create a text-based application that submits YouTube queries, allowing the user to view various statistical information about videos.

## Background

Since 2005, YouTube has allowed the public submission of videos, providing a simple platform for users to share their creations. In more recent times, viral videos and YouTube personalities have made an impact on society. With the rise in popularity, a great deal of videos are uploaded and viewed every minute generating an immense amount of statistical data. YouTube provides a means of third-party applications to “scrape” this data. In this project, we will generate and submit queries to retrieve and view the current state of YouTube videos.

Project Description / Specification

Your program will allow the user to generate a YouTube query for:
- Top Rated
- Top Favorites
- Most Viewed
- Most Recent
- Most Discussed

The user may specify the number of results they wish the query to be restricted by. Information received from the query will be displayed on screen in a readable fashion. In addition to basic video information, you will also display extra information about the user who uploaded the video.

In order to easily track and store information obtained from the query, you will use 3 classes:
- Query
- Video
- User

The Query class will store the results, i.e., videos, produced for a single query request from the user. It is also responsible for calculating general statistics regarding the results. The Video class stores basic information about a single video. Similarly, the User class will store various information about the YouTube user who submitted the related video.

YouTube Queries
To perform the queries, we will use the Google Data API (see [http://code.google.com/apis/youtube/getting_started.html#data_api](http://code.google.com/apis/youtube/getting_started.html#data_api)). The API is used by sending well-defined HTTP requests, which returns an XML stream containing the results. The Data API has been thoroughly developed and contains a lot of features for doing just anything with the YouTube website; however, we will only deal with a small subset of these features.

In order to communicate with API, we can use the **requests** module to send HTTP requests and to read the responses. The request is sent using the ***get()*** or ***post()*** methods that takes a string containing the URL. A file-like object is returned and used to read the response.

A list of the base URLs to use in order to fulfill the query options are listed below and at [http://code.google.com/apis/youtube/2.0/reference.html#Standard_feeds](http://code.google.com/apis/youtube/2.0/reference.html#Standard_feeds)

## Query Class

The Query class will perform the actual HTTP request and initial parsing to build the Video objects from the response. It will also calculate the following information based on the video and user results.

- Video Data
    - Total Video Favorite Count (favoriteCount)
    - Total Video View Count (viewCount)
- User Data
    - Total User Subscriber Count (subscriberCount)
    - Total User Upload View Count (totalUploadViews)



## Required Functions

```python
__init__(self, feed_id, max_results): #Takes as input the type of query (feed_id) and the maximum number of results (max_results) that the query should obtain. The correct HTTP request must be constructed and submitted. The results are converted into Video objects, which are stored within this class.
```

```python
__str__(self): #Prints out information on each video and YouTube user, including the aforementioned statistics data.
```

## User Class

The User class will perform another query to obtain detailed information about the uploader of a video. This class will store:
- Username (name)
- Number of Subscribers (subscriberCount)
- Total Views of Uploaded Videos (totalUploadViews)

## Required Functions
```python
	__init__(self, author_str): #The author_str will contain the text encapsulated in the <author> tag of an <entry>. The string must be parsed to extract the YouTube username of the Video’s uploader. Another HTTP request must be constructed and submitted to obtain the extra information about the uploader.

	__str__(self): #Include this function to display the stored data about the user.
```


# Video Class
The Video class tracks information about a single YouTube video. This class will store:
- Title (media:title)
- User instance
- Description (media:description)
- Favorite Count (favoriteCount)
- Total Views (viewCount)

## Required Functions

```python
__init__(self, entry_str): #The entry_str will contain the text encapsulated in a single <entry> section. The string must be parsed to extract the various pieces of information and the text to create the User instance.

__str__(self): #Include this function to display the stored Video data, as well as data for the associated uploader.
```


## Main function

The *main()* function in your program should prompt the user with a choice to select a query on one of the previously mentioned feeds (top rated, most discussed, …). They should also be prompted for the maximum number of results. Results of the query are displayed, and the user is reprompted for another query until they select to quit. Error checking is to be performed on all input, with reprompts for invalid values.

## Example Run

```
Welcome to the YouTube text-based query application.
You can select a popular feed to perform a query on and view statistical information about the related videos and users.

1) today
2) this week
3) this month
4) since youtube started

Please select a time(or 'Q' to quit):1

1) Top Rated
2) Top Favorited
3) Most Viewed
4) Most Recent
5) Most Discussed

Please select a feed (or 'Q' to quit): 1
Enter the maximum number of results to obtain: 2

********************************************************************************
                                Top Rated Videos                                
********************************************************************************

********************************************************************************
Title: Minecraft - "Shadow of Israphel" Part 35: Lastwatch Hold (Minecon Special!)
Views: 903,180
Favorited: 4,907

Uploader: BlueXephos
Author's Statistics:
Subscriber Count: 1,222,878
Total Upload Views: 527,462,846

********************************************************************************

********************************************************************************
Title: Overcrowded Minecraft Farm!?
Views: 113,096
Favorited: 10,819

Uploader: TheSyndicateProject
Author's Statistics:
Subscriber Count: 585,493
Total Upload Views: 182,663,315

********************************************************************************

--------------------------------------------------------------------------------
                        Total Favorited:          15,726
                           Total Viewed:       1,016,276
                       Total Subscribed:       1,808,371
         Total Views of Uploaded Videos:     710,126,161
--------------------------------------------------------------------------------

1) today
2) this week
3) this month
4) since youtube started

Please select a time(or 'Q' to quit):4

1) Top Rated
2) Top Favorited
3) Most Viewed
4) Most Recent
5) Most Discussed

Please select a feed (or 'Q' to quit): 2
Enter the maximum number of results to obtain: 2

********************************************************************************
                              Top Favorited Videos                              
********************************************************************************

********************************************************************************
Title: Evolution of Dance - By Judson Laipply
Views: 184,334,352
Favorited: 1,085,632

Uploader: judsonlaipply
Author's Statistics:
Subscriber Count: 72,597
Total Upload Views: 187,215,602

********************************************************************************

********************************************************************************
Title: Charlie bit my finger - again !
Views: 389,866,571
Favorited: 1,046,159

Uploader: HDCYT
Author's Statistics:
Subscriber Count: 161,895
Total Upload Views: 501,782,556

********************************************************************************

--------------------------------------------------------------------------------
                        Total Favorited:       2,131,791
                           Total Viewed:     574,200,923
                       Total Subscribed:         234,492
         Total Views of Uploaded Videos:     688,998,158
--------------------------------------------------------------------------------

1) today
2) this week
3) this month
4) since youtube started

Please select a time(or 'Q' to quit):q
>>>
```