Title: Felix: a PHP / Twilio Group Messaging Tool
Date: 2014-07-14
Summary: Keep the whole group in the loop.
Slug: group-texting-with-php-and-twilio
Tags: Twilio, PHP, SMS

### Keep the whole group in the loop

During my first year as an Industry Advisor at <a href="http://www.businesshorizonsiowa.org/">Business Horizons</a> (a week-long summer program for Iowa high school students) it occurred to me that we really didn't have a way for everyone to quickly get messages to the group in the event of a schedule change or emergency.

There were about 20 or so advisors. Some had iPhones, some had Androids, and some had flip-phones. 

In just a couple hours, I put together a SMS tool using <a href="http://twilio.com">Twilio</a> that we've used for the last two years.

Recently, I updated the tool to use <a href="https://github.com/twilio/twilio-php">Twilio's updated PHP library</a>, put <a href="https://github.com/alexpgates/felix">everything on Github</a>, and named it after my 6-week old baby boy.

### No smartphone required

Felix could be very useful for event organizers, summer camp counselors, schools, or anyone looking for an easy and inexpensive way to keep a group connected without requiring anyone to download an app or own a smartphone.

### Features

- The onboarding flow allows users to join the group by texting anything to the number, then following simple directions.
- Members can leave the group by sending: <code>-stop</code>
- Members can change their nicknames by sending: <code>-name</code>, followed by their new nickname.
- The group administrator receives an alert when new members join.
- All messages are logged in the database.
- Messages can contain up to 1600 characters.

### Join Flow

Members join the group by texting anything to the phone number. After replying with your name, you're all set.

<div class="row text-center">
    <img src="/static/images/felix-join-flow.png" width="300px">
</div>

### Use

As you can see, Felix is also handy for some good old trash-talking.

<div class="row text-center">
    <img src="/static/images/felix-use.png" width="300px">
</div>

### Requirements &amp; Setup

Felix requires a Twilio account, a verified phone number, MySQL, PHP, and a web host. Everything you need to know can be found on <a href="https://github.com/alexpgates/felix">the Github page</a>.

---

### Give it a try!

Feel free to shoot me an email if you have any questions or run in to any issues. If you fix any bugs or add any features, send me a pull request on Github!

If this came in handy for your event, I'd love to hear about it!

<div class="row text-center top-padding download">
    <a class="btn btn-large" href="https://github.com/alexpgates/felix/archive/master.zip">Download Felix <i class="fa fa-arrow-circle-right"></i></a>
</div>