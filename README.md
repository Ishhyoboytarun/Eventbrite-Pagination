
# Pagination Abstraction

## Problem Description

The problem involves adapting a third-party web service to follow a specific pagination policy. The web service only accepts a page number and returns 10 items per page, without any metadata. The goal is to adapt the service to conform to a pagination policy that includes metadata and accepts a specific number of items per page. The pagination policy requires that methods returning more than 50 records should be paged and should return an object including metadata that describes the total count of items, the page number, the number of items per page, and an array of items for the given page. The method should accept a page number and the number of items per page, and should return the string "404" when a page is requested that does not exist.

## Pagination Policy

1. Methods returning more than 50 records should be paged.
2. Paged methods should return an object including meta data
  a) total _count gives the total count of items available in the service
  b) page_number echoes the page requested
  c) items_per_page echoes the number of items in a page requested
  d) items is an array of the items for the given page
3. Paged methods should accept
  a) page_number defining which page of data to return
    • page _number is 1-indexed, meaning the first page of valid results is page 1
  b) items_per_page defining the number of items on any given page
4. Paged methods should return the string "404" when a page is requested that does not exist.

## Solution

The code solution involves writing a function called `abstracted_request` that takes a page number and the number of items per page as input. The function calls a `get_request` function that accepts only a page number and returns 10 items per page. The `abstracted_request` function adapts the output of `get_request` to conform to the pagination policy by adding metadata and returning an object that includes the total count of items, the page number, the number of items per page, and an array of items for the given page.

The `abstracted_request` function checks if the page number and the number of items per page are valid, and returns the string "404" when a page is requested that does not exist. The `format_response` function is used to format the output of the `get_request` function into an object that includes metadata.

## How to Use

To use the `abstracted_request` function, simply call it with a page number and the number of items per page as input. The function will return an object that includes metadata about the items on the given page. 

For example, to get the first page of items with 20 items per page, call the function with `abstracted_request(1, 20)`. 

If a page that does not exist is requested, the function will return the string "404".
