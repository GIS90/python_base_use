# Tour Lead CRUD Test

## Overview

This test is for a simple Django CRUD views to add, edit and display tour leaders.

UI mockup is in [crud-test.html](crud-test.html).

Just implement as much functionality as you can in a time-box of 2 hours focusing fist on quality rather than quantity.

There're a lot of requirements so you're not expected to complete all of them, implement what you can and do it well,
And don't leave half implemented code and functionality, remove anything that's not completely finished in the final result.

At least the fist function (Add Lead) has to be implemented perfectly from every perspective (function, logic, code quality, tests, UX).

## Functionality to implement (in order of priority)

### 1. Add Tour Lead view

![](https://www.evernote.com/l/AHR6kVOimNhEAptuqzsASeKXsCVHHXON5VwB/image.png)

It should be with languages as inline formset where languages can be added/removed in the list.

![](https://www.evernote.com/l/AHSY8s1byANBk7YjdpsjcLT9dkai28MYDcwB/image.png)

Fields:

* Name
    - Required
* Gender
    - Required
    - Widget: horizontal radio buttons
* Languages
    - Required: at least one language should be added
    - Widget: Inline formset
* Card number
    - Length: 8-15
    - Only numbers and capital letters: X, T, W are allowed
* Expiry date
    - Required if Card number is not empty
    - Has to be at least 6 months into the future
    - Widget: Datepicker
* Professional
    - Required
    - Widget: horizontal radio buttons

### 2. Tour Leads List view

![](https://www.evernote.com/l/AHRlRb8RWsxI4ZfsCMdDawIptRNdWTCOtD0B/image.png)

### 3. Edit Tour Lead view

Same as add

### 4. Tour Lead Detail view

![](https://www.evernote.com/l/AHSPFjRgvBROzamFG2_cvifetmFCZ-6CTgoB/image.png)

### 5. Delete Tour Lead

![](https://www.evernote.com/l/AHTpOW13eelOX44ZWOaG8psPjLFeGKvKUvYB/image.png)

### 6. Pagination

![](https://www.evernote.com/l/AHQPkBVV1X5DaaiUWL0TaQTHeU6DyIzbuqsB/image.png)

### 7. Batch Delete

![](https://www.evernote.com/l/AHSsX1ZWe5hC2piuYM7Yk5rQJGBkwTujGNcB/image.png)

## Project setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run django server:

```
./manage.py runserver
```

3. Open http://localhost:8000/leads/ in a browser

## Good Luck!
